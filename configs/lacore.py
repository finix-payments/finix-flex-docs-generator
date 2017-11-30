import base64
from collections import OrderedDict

partner_configs = {
        'api_name': "Lacore",
        'api_name_downcase': "lacore",
        'admin_basic_auth_username': 'USd6r7ERYMsK2mDUBmqWdhmk',
        'admin_basic_auth_password': 'b271aac5-6826-4d2d-af66-bf86e9ffa85b',
        'platform_basic_auth_username': 'USd6r7ERYMsK2mDUBmqWdhmk',
        'platform_basic_auth_password': 'b271aac5-6826-4d2d-af66-bf86e9ffa85b',
        'platform_encoded_auth': base64.b64encode('USd6r7ERYMsK2mDUBmqWdhmk:b271aac5-6826-4d2d-af66-bf86e9ffa85b'),
        'admin_encoded_auth': base64.b64encode('USd6r7ERYMsK2mDUBmqWdhmk:b271aac5-6826-4d2d-af66-bf86e9ffa85b'),
        'basic_auth_username': None,
        'basic_auth_password': None,
        'encoded_auth': None,
        'payment_processor': "DUMMY_V1",
        'identity_verification_processor': "DUMMY_V1",
        'jsfiddle': "http://jsfiddle.net/rserna2010/2hxnjL0q/",
        'embedded_iframe_src': "https://vgs-assets.s3.amazonaws.com/payline-1.latest.js",
        'embedded_iframe_jsfiddle': "https://jsfiddle.net/ne96gvxs/",
        'staging_base_url': "https://lacore-sandbox.finixpayments.com",
        'production_base_url': "https://api.live.lacore.finixpymnts.com",
        'python_client_resource_name': "lacore",
        'php_client_repo': "https://github.com/Payline/payline-php",
        'php_client_resource_name': "Lacore",
        'ruby_client_resource_name': "Lacore",
        'ruby_gem': "payline-data",
        'ruby_require_statement': "payline",
        'java_artifact_id': "payline-data",
        'hosted_fields_src': "https://js.verygoodvault.com/js-vgfield-2/payline.js",
        'hosted_fields_jsfiddle': "https://jsfiddle.net/rserna2010/vap35hru/",
        }

# this provides the ordering for the docs by section and individual snippet
# Doc Type: [NON-ADMIN]
snippets_by_resource = {
    "api_endpoints": [
        "definition",
        ],
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
        "list_authorizations",
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
        ],
    "guide_general_overview_no_payouts": [
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
    "guide_hosted_fields": [
        "definition",
        "associate_token",
        ],
    "test_data": [
        "definition"
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
        # "create_merchant_user",
        "reattempt_merchant_provision",
        "update_merchant_on_processor",
        "list_merchants",
        "list_merchant_verifications",
        ],
    "payment_instruments": [
        "definition",
        "create_card",
        "create_bank_account",
        "associate_token",
        "fetch_bank_account",
        "fetch_credit_card",
        "check_card_updater",
        # "update_payment_instrument",
        "list_payment_instruments",
        ],
    "settlements": [
        "definition",
        "create_settlement",
        "fetch_settlement",
        "remove_transfer",
        # "fund_settlement",
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
        "update_transfer",
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
    "idempotent_requests": [
        "definition",
    ],
    "topics": [
    'definition',
    ],
    'tags': [
        'definition',
    ],
    'errors': [
        'definition'
    ]
}

# this provides the ordering for the docs by section and individual snippet
# Doc Type: ADMIN LEVEL
admin_snippets_by_resource = {
    "api_endpoints": [
        "definition",
        ],
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
    "guide_general_overview_no_payouts": [
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
    "guide_hosted_fields": [
        "definition",
        "associate_token",
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
        "associate_token",
        "create_card",
        "create_bank_account",
        "fetch_bank_account",
        "fetch_credit_card",
        "check_card_updater",
        # "update_payment_instrument",
        "list_payment_instruments",
        ],
    "settlements": [
        "definition",
        "create_settlement",
        "fetch_settlement",
        "remove_transfer",
        "fund_settlement",
        "list_settlements",
        "list_settlement_funding_transfers",
        "list_settlement_transfers",
        ],
    "guide_tokenization_js": [
        "definition",
        "associate_token",
        ],
    "test_data": [
        "definition"
    ],
    "transfers": [
        "definition",
        # "create_debit",
        "create_bank_debit",
        "fetch_transfer",
        "create_refund",
        "list_transfers",
        "update_transfer",
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
    "fees": [
        "definition"
    ],
    "idempotent_requests": [
        "definition",
    ],
    "topics": [
    'definition',
    ],
    'tags': [
        'definition',
    ],
    'errors': [
        'definition'
    ]
}

# This is the order that the directories / guides will be concatinated
resource_ordering = [
    "topics",
    "api_endpoints",
    "guide_authentication",
    "idempotent_requests",
    "tags",
    "test_data",
    "errors",
    "guide_general_overview_no_payouts",
    "guide_getting_started",
    "guide_iframe",
    "guide_hosted_fields",
    "idempotent_requests",
    # "guide_tokenization_js",
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
    "topics",
    "api_endpoints",
    "guide_authentication",
    "idempotent_requests",
    "tags",
    "test_data",
    "errors",
    "fees",
    "guide_general_overview_no_payouts",
    "guide_getting_started",
    "guide_iframe",
    "guide_hosted_fields",
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
# https://github.com/lord/slate/wiki/Customizing-the-Language-Tabs
# KEY: maps to the perferred tab name in the templates & filing naming convention
#      structure for scenarios
# VALUE: maps to the language_tab value in slate

included_clients = OrderedDict([
    ("cURL", "shell"),
    ("Java", "java"),
    ("PHP", "php"),
    ("Python", "python"),
    ("Ruby", "ruby"),
])