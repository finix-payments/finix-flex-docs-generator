import base64

partner_configs = [
    {
        'api_name': "Finix",
        'api_name_downcase': "finix",
        'base_url': 'https://api-staging.finix.io',
        'admin_basic_auth_username': 'US7AQLoX6FtZcPDttFAafEz2',
        'admin_basic_auth_password': 'f3276399-20f4-4bc3-aff0-71131cb347b8',
        'admin_encoded_auth': base64.b64encode('US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8'),
        'platform_basic_auth_username': 'US9C35Uh2qqqWLiaCHbMBb4c',
        'platform_basic_auth_password': 'a821faf7-625a-4ab8-943e-f5e8ef94b834',
        'platform_encoded_auth': base64.b64encode('US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834'),
        'payfac_username': "FINIXDATAMP",
        'basic_auth_username': None,
        'basic_auth_password': None,
        'encoded_auth': None,
        'payment_processor': "DUMMY_V1",
        'identity_verification_processor': "DUMMY_V1",
        'application': None,
        'jsfiddle': "http://jsfiddle.net/rserna2010/2hxnjL0q/",
        'embedded_iframe_src': "https://vgs-assets.s3.amazonaws.com/payline-1.latest.js",
        'embedded_iframe_jsfiddle': "https://jsfiddle.net/ne96gvxs/",
        },
    # {
    #     'api_name': "Payline",
    #     'api_name_downcase': "payline",
    #     'base_url': 'https://api-test.payline.io',
    #     'admin_basic_auth_username': 'USkoFNY73WEiP8tYmZtPa6e4',
    #     'admin_basic_auth_password': 'e28fe471-5b2c-4f20-9db9-0a3e5fd06110',
    #     'platform_basic_auth_username': 'USjXwXbL7N1tp6UnCCqfogkP',
    #     'platform_basic_auth_password': '8d745c00-1f4f-4d65-a92c-44dcf19e872e',
    #     'platform_encoded_auth': base64.b64encode('USjXwXbL7N1tp6UnCCqfogkP:8d745c00-1f4f-4d65-a92c-44dcf19e872e'),
    #     'payfac_username': "PAYLINEDATAMP",
    #     'admin_encoded_auth': base64.b64encode('USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110'),
    #     'basic_auth_username': None,
    #     'basic_auth_password': None,
    #     'encoded_auth': None,
    #     'payment_processor': "DUMMY_V1",
    #     'identity_verification_processor': "DUMMY_V1",
    #     'application': None,
    #     'jsfiddle': "http://jsfiddle.net/rserna2010/sab76Lne/",
    #     'embedded_iframe_src': "https://vgs-assets.s3.amazonaws.com/payline-1.latest.js",
    #     'embedded_iframe_jsfiddle': "https://jsfiddle.net/rserna2010/47kgeao9/",
    #     },
    # {
    #     'api_name': "SimonPay",
    #     'api_name_downcase': "simonpay",
    #     'base_url': 'https://api-staging.simonpayments.com',
    #     'admin_basic_auth_username': 'USkq2yiDni9oFNpcuRNDMPmA',
    #     'admin_basic_auth_password': 'b559b81b-5b6e-4e22-aba5-81fd12265314',
    #     'admin_encoded_auth': base64.b64encode('USkq2yiDni9oFNpcuRNDMPmA:b559b81b-5b6e-4e22-aba5-81fd12265314'),
    #     'platform_basic_auth_username': 'USkq2yiDni9oFNpcuRNDMPmA',
    #     'platform_basic_auth_password': 'b559b81b-5b6e-4e22-aba5-81fd12265314',
    #     'platform_encoded_auth': base64.b64encode('USkq2yiDni9oFNpcuRNDMPmA:b559b81b-5b6e-4e22-aba5-81fd12265314'),
    #     'payfac_username': "SIMONPAY",
    #     'basic_auth_username': None,
    #     'basic_auth_password': None,
    #     'encoded_auth': None,
    #     'payment_processor': "DUMMY_V1",
    #     'identity_verification_processor': "DUMMY_V1",
    #     'application': None,
    #     'jsfiddle': "http://jsfiddle.net/rserna2010/sab76Lne/",
    #     'embedded_iframe_src': "https://vgs-assets.s3.amazonaws.com/payline-1.latest.js",
    #     'embedded_iframe_jsfiddle': "https://jsfiddle.net/rserna2010/1626475h/",
    # },
]


# this provides the ordering for the docs by section and individual snippet
# Doc Type: [NON-ADMIN]
snippets_by_resource = {
    "applications": [
        "definition",
        "create_application",
        "fetch_application",
        # "enable_dummy_processor",
        # "enable_litle_processor",
        # "disable_application",
        "create_partner_user",
        "list_applications",
        ],
    "authorizations": [
        "definition",
        "create_authorization",
        "capture_authorization",
        "void_authorization",
        "fetch_authorization",
        "list_authorizations"
    ],

    "disputes": [
        "definition",
        # "create_dispute",
        "fetch_dispute",
        "list_disputes"
    ],
    "guide_admin_overview": [
        "definition",
        ],
    "guide_create_application": [
        "definition",
        "create_owner_user",
        "create_application",
        "enable_dummy_processor",
        ],
    "guide_general_overview": [
        "definition",
        ],
    "guide_getting_started": [
        "definition",
        "create_merchant_identity",
        "create_bank_account",
        # "perform_identity_verification",
        "provision_merchant",
        "create_buyer_identity",
        "create_card",
        # "create_card_debit",
        "create_authorization",
        "capture_authorization",
        "create_batch_settlement",
        # "fund_settlement",
        # "refund_debit"
    ],
    "guide_iframe": [
        "definition",
        "associate_token",
        ],
    "guide_push_to_card": [
        "definition",
        "create_recipient_identity",
        "create_card",
        "send_to_recipient",
        ], 
    "identities": [
        "definition",
        "create_buyer_identity",
        "create_merchant_identity",
        "fetch_identity",
        "list_identities",
        "update_identity",
        "provision_merchant",
        ],
    "merchants": [
        "definition",
        "provision_merchant",
        "fetch_merchant",
        "create_merchant_user",
        "reattempt_merchant_provision",
        "update_merchant_on_processor",
        "list_merchants",
        "list_merchant_verifications",
        ],
    "payment_instruments": [
        "definition",
        "create_card",
        "create_bank_account",
        "tokenize_card_iframe",
        "associate_token",
        "fetch_payment_instrument",
        "update_payment_instrument",
        "list_payment_instruments",
        ],
    "settlements": [
        "definition",
        "create_settlement",
        "fetch_settlement",
        "fund_settlement",
        "list_settlements",
        "list_settlement_funding_transfers",
        "list_settlement_transfers",
        ],
    "guide_tokenization_js": [
        "definition",
        "associate_token",
        ],

    "transfers": [
        "definition",
        # "create_debit",
        "fetch_transfer",
        "create_refund",
        "list_transfers",
        ],
    "users": [
        "definition",
        "create_partner_user",
        "create_merchant_user",
        "disable_user",
        "fetch_user",
        "list_users"
    ],
    "webhooks": [
        "definition",
        "create_webhook",
        "fetch_webhook",
        "list_webhooks",
        "sample_payloads",
        ],
    }

# this provides the ordering for the docs by section and individual snippet
# Doc Type: ADMIN LEVEL
admin_snippets_by_resource = {
    "applications": [
        "definition",
        "fetch_application",
        "create_application",
        "disable_application_processing",
        "disable_application_settlements",
        "create_partner_user",
        "enable_dummy_processor",
        # "enable_litle_processor",
        "list_applications",
        ],
    "authorizations": [
        "definition",
        "create_authorization",
        "capture_authorization",
        "void_authorization",
        "fetch_authorization",
        "list_authorizations"
    ],

    "disputes": [
        "definition",
        # "create_dispute",
        "fetch_dispute",
        "list_disputes"
    ],
    "guide_admin_overview": [
        "definition",
        ],
    "guide_authentication": [
        "definition",
        "authentication",
        ],
    "guide_create_application": [
        "definition",
        "create_owner_user",
        "create_application",
        "enable_dummy_processor",
        "enable_processing",
        "enable_settlements",
        ],
    "guide_general_overview": [
        "definition",
        ],
    "guide_getting_started": [
        "definition",
        "create_merchant_identity",
        "create_bank_account",
        # "perform_identity_verification",
        "provision_merchant",
        "create_buyer_identity",
        "create_card",
        # "create_card_debit",
        "create_authorization",
        "capture_authorization",
        "create_batch_settlement",
        # "fund_settlement",
        # "refund_debit"
    ],
    "guide_iframe": [
        "definition",
        "associate_token",
        ],
    "guide_push_to_card": [
        "definition",
        "create_recipient_identity",
        "create_card",
        "send_to_recipient",
        ],        
    "identities": [
        "definition",
        "create_buyer_identity",
        "create_merchant_identity",
        "fetch_identity",
        "update_identity",
        "list_identities",
        ],
    "merchants": [
        "definition",
        "provision_merchant",
        "fetch_merchant",
        "update_merchant_on_processor",
        "reattempt_merchant_provision",
        "disable_merchant_processing",
        "disable_merchant_settlements",
        "list_merchants",
        "list_merchant_verifications",
        "list_merchant_verifications_platform_user",
        "create_merchant_user",
        ],
    "payment_instruments": [
        "definition",
        "tokenize_card_iframe",
        "associate_token",
        "create_card",
        "create_bank_account",
        "fetch_payment_instrument",
        "update_payment_instrument",
        "list_payment_instruments",
        ],
    "settlements": [
        "definition",
        "create_settlement",
        "fetch_settlement",
        "fund_settlement",
        "list_settlements",
        "list_settlement_funding_transfers",
        "list_settlement_transfers",
        ],
    "guide_tokenization_js": [
        "definition",
        "associate_token",
        ],

    "transfers": [
        "definition",
        # "create_debit",
        "create_bank_debit",
        "fetch_transfer",
        "create_refund",
        "list_transfers",
        ],
    "users": [
        "definition",
        "create_partner_user",
        "create_merchant_user",
        "fetch_user",
        "disable_user",
        "list_users"
    ],
    "webhooks": [
        "definition",
        "create_webhook",
        "fetch_webhook",
        "list_webhooks",
        "sample_payloads",
        ],
    }

# This is the order that the directories / guides will be concatinated
resource_ordering = [
    "guide_general_overview",
    "guide_getting_started",
    "guide_iframe",
    "guide_push_to_card",
    "authorizations",
    # "disputes",
    "identities",
    "merchants",
    "payment_instruments",
    # # "identity_verifications",
    "settlements",
    "transfers",
    "webhooks",

]

admin_resource_ordering = [
    "guide_general_overview",
    "guide_authentication",
    "guide_getting_started",
    "guide_iframe",
    "guide_getting_started",
    "guide_admin_overview",
    "guide_create_application",
    "guide_tokenization_js",
    "applications",
    "authorizations",
    # "disputes",
    "identities",
    # # "identity_verifications",
    "merchants",
    "payment_instruments",
    "settlements",
    "transfers",
    "users",
    "webhooks",
    ]



# Determine which client libraries to include
included_clients = [
    "curl",
    "php",
    "java"
]