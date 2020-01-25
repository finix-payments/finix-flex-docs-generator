import base64
from collections import OrderedDict

partner_configs = {
        'api_name': "Finix",
        'api_name_downcase': "finix",
        'admin_basic_auth_username': 'US7AQLoX6FtZcPDttFAafEz2',
        'admin_basic_auth_password': 'f3276399-20f4-4bc3-aff0-71131cb347b8',
        'admin_encoded_auth': base64.b64encode('US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8'),
        #
        # 'platform_basic_auth_username': 'USimz3zSq5R2PqiEBXY6rSiJ',
        # 'platform_basic_auth_password': '8bacba32-9550-48ff-b567-fe7648947041',
        # 'platform_encoded_auth': base64.b64encode('USimz3zSq5R2PqiEBXY6rSiJ:8bacba32-9550-48ff-b567-fe7648947041'),
        #
        # 'platform_basic_auth_username': 'USpTNdGq7qfgVwCHHP9gKoSu',
        # 'platform_basic_auth_password': 'a4c1e20e-bc44-405e-9df4-82fce5a4d3c9',
        #
        # 'platform_basic_auth_username_payouts': 'US8HXXhg1hakavFEhNzpzLHk',
        # 'platform_basic_auth_password_payouts': '1bb1f91a-5e65-4667-bcb7-55d6fa1c0c79',
        # 'platform_encoded_auth_payouts': base64.b64encode('US8HXXhg1hakavFEhNzpzLHk:1bb1f91a-5e65-4667-bcb7-55d6fa1c0c79'),

        #QA
        'platform_basic_auth_username': 'USdKBJ2TFYKDL9zCP7T9rbkj',
        'platform_basic_auth_password': 'f5498da8-58f6-45c7-8a61-afe55c4073d4',
        'platform_encoded_auth': base64.b64encode('USdKBJ2TFYKDL9zCP7T9rbkj:f5498da8-58f6-45c7-8a61-afe55c4073d4'),

        'platform_basic_auth_username_payouts': 'USdKBJ2TFYKDL9zCP7T9rbkj',
        'platform_basic_auth_password_payouts': 'f5498da8-58f6-45c7-8a61-afe55c4073d4',
        'platform_encoded_auth_payouts': base64.b64encode('USdKBJ2TFYKDL9zCP7T9rbkj:f5498da8-58f6-45c7-8a61-afe55c4073d4'),


        'basic_auth_username': None,
        'basic_auth_password': None,
        'encoded_auth': None,
        'basic_auth_username_payouts': None,
        'basic_auth_password_payouts': None,
        'encoded_auth_payouts': None,
        'payment_processor': "DUMMY_V1",
        'identity_verification_processor': "DUMMY_V1",
        'jsfiddle': "http://jsfiddle.net/rserna2010/2hxnjL0q/",
        'embedded_iframe_src': "https://forms.finixpymnts.com/finix.js",
        'window.PaymentForm': "Finix",
        'embedded_iframe_jsfiddle': "https://jsfiddle.net/ne96gvxs/27/",
        # 'staging_base_url': "https://finix.sandbox-payments-api.com",
        'staging_base_url': "https://finix.qa-payments-api.com",
        'live_base_url': "https://finix.live-payments-api.com",
        'python_client_resource_name': "finix",
        'php_client_repo': "https://github.com/finix-payments/processing-php-client",
        'php_client_resource_name': "Finix",
        'ruby_client_resource_name': "Finix",
        'ruby_gem': "finix",
        'ruby_require_statement': "finix",
        'java_artifact_id': "finix",
        'version': '1.0.6',
        'java_group_id': "io.finix.payments.processing.client",
        'hosted_fields_src': "https://forms.finixpymnts.com/finix.js",
        'hosted_fields_jsfiddle': "https://jsfiddle.net/maserna2/znLe9kp6/",
        'ACH_business_day_delay': '3'
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
        "triPOS_Authorization_with_EMV_card",
        "triPOS_Authorization_with_Non_EMV_card",
        "triPOS_Capture_Authorization",
        "fetch_authorization",
        "list_authorizations"
    ],

    "disputes": [
        "definition",
        "upload_dispute",
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
    "guide_general_overview_finix": [
        "definition",
        ],
    "guide_getting_started": [
        "definition",
        "create_merchant_identity",
        "create_bank_account",
        # "perform_identity_verification",
        "provision_merchant",
        "create_buyer_identity",
        "create_payment_card",
        # "create_card_debit",
        "create_authorization",
        "capture_authorization",
        # "create_batch_settlement", uncomment
        # "fund_settlement",
        # "refund_debit"
    ],
    # "guide_iframe": [
    #     "definition",
    #     "associate_token",
    # ],
    "guide_hosted_fields_payouts": [
        "definition",
        "associate_token",
    ],
    "guide_mobile": [
        "definition",
        "guide_android",
        "guide_iOS",
    ],
    "guide_push_to_card": [
        "definition",
        "create_recipient_identity",
        "create_payment_card",
        "verify_card",
        "provision_merchant_account",
        "send_to_recipient",
        ],
    "guide_pull_from_card": [
        "definition",
        "create_sender_identity",
        "create_payment_card",
        "verify_card",
        "provision_merchant_account",
        "pull_from_sender",
        "create_refund",
        # "send_to_recipient",
        ],
    "guide_tripos": [
        "definition",
        "Provision_Merchant_with_triPOS",
        "triPOS_Create_Device",
        "triPOS_Activate_Device",
        "triPOS_Authorization_with_EMV_card",
        "triPOS_Capture_Authorization",
        ],
    "fee_profile_overview": [
        "definition",
        ],
    'guide_application_fee_profiles': [
        "definition",
        '1_create_new_profile',
        '2_locate_application_profile',
        '3_update_application_profile',
    ],
    'guide_merchant_fee_profiles': [
        "definition",
        '1_create_new_profile',
        '2_locate_merchant',
        '3_locate_merchant_profile',
        '4_update_merchant_profile',
    ],
    'guide_risk_profiles': [
        "definition",
        '1_locate_merchant',
        '2_locate_merchant_profile',
        '3_update_risk_profile',
    ],
    "test_data_finix": [
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
    "devices": [
        "definition",
        "triPOS_Create_Device",
        "triPOS_Activate_Device",
        "Fetch_triPOS_Device",
        "Reboot_triPOS_Device",
        "Set_Idle_Message_on_triPOS_Device",
        "Check_Connectivity_of_triPOS_Device",
        "Deactivate_triPOS_Device",
    ],
    "merchants": [
        "definition",
        "provision_merchant",
        "fetch_merchant",
        # "create_merchant_user",
        "reattempt_merchant_provision",
        "Provision_Merchant_with_triPOS",
        "update_merchant_on_processor",
        "list_merchants",
        "list_merchant_verifications",
        ],
    "payment_instruments": [
        "definition",
        "create_payment_card",
        "create_bank_account",
        "associate_token",
        "fetch_bank_account",
        "fetch_payment_card",
        # "update_payment_instrument",
        "check_card_updater",
        "list_payment_instruments",
        "verification",
        ],
    "settlements": [
        "definition",
        "create_settlement",
        "fetch_settlement",
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
        "triPOS_Sale_with_EMV_Card",
        "triPOS_Sale_using_Non_EMV_Card",
        "triPOS_Sale_with_Manual_Entry",
        "Referenced_Refund",
        "Unreferenced_Refund_with_Swipe_Card",
        "list_transfers",
        "update_transfer",
        ],
    # "users": [
    #     "definition",
    #     "create_partner_user",
    #     "create_merchant_user",
    #     "disable_user",
    #     "fetch_user",
    #     "list_users"
    # ],
    "webhooks": [
        "definition",
        "create_webhook",
        "update_webhook",
        "fetch_webhook",
        "list_webhooks",
        "sample_payloads",
        ],
    "fees": [
        "definition"
    ],
    "dashboard_overview_finix": [
        "definition"
    ],
    "idempotent_requests": [
        "definition",
    ],
    "topics": [
        'definition'
    ],
    'tags': [
        'definition',
    ],
    'errors_payouts': [
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
        "create_partner_user",
        "create_application",
        "disable_application_processing",
        "disable_application_settlements",
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
        "upload_dispute",
        "fetch_dispute",
        "list_disputes"
    ],
    "guide_admin_overview": [
        "definition",
        ],
    "fee_profile_overview": [
        "definition",
        ],
    'guide_application_fee_profiles': [
        "definition",
        '1_create_new_profile',
        '2_locate_application_profile',
        '3_update_application_profile',
    ],
    'guide_merchant_fee_profiles': [
        "definition",
        '1_create_new_profile',
        '2_locate_merchant',
        '3_locate_merchant_profile',
        '4_update_merchant_profile',
    ],
    'fee_profile': [
        "fetch_fee_profile"
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
    "guide_general_overview_finix": [
        "definition",
        ],
    "guide_getting_started": [
        "definition",
        "create_merchant_identity",
        "create_bank_account",
        # "perform_identity_verification",
        "provision_merchant",
        "create_buyer_identity",
        "create_payment_card",
        # "create_card_debit",
        "create_authorization",
        "capture_authorization",
        "create_batch_settlement",
        # "fund_settlement",
        # "refund_debit"
    ],
    # "guide_iframe": [
    #     "definition",
    #     "associate_token",
    # ],
    "guide_hosted_fields_payouts": [
        "definition",
        "associate_token",
    ],
    "guide_mobile": [
        "definition",
        "guide_android",
        "guide_iOS",
    ],
    "guide_push_to_card": [
        "definition",
        "create_recipient_identity",
        "create_payment_card",
        "verify_card",
        "provision_merchant_account",
        "send_to_recipient",
        ],
    "guide_pull_from_card": [
        "definition",
        "create_sender_identity",
        "create_payment_card",
        "verify_card",
        "provision_merchant_account",
        "pull_from_sender",
        # "send_to_recipient",
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
        "ready_to_settle_upon_capture",
        "list_merchants",
        "list_merchant_verifications",
        "list_merchant_verifications_platform_user",
        # "create_merchant_user",
        ],
    "payment_instruments": [
        "definition",
        "associate_token",
        "create_payment_card",
        "create_bank_account",
        "fetch_bank_account",
        "fetch_payment_card",
        # "update_payment_instrument",
        "check_card_updater",
        "list_payment_instruments",
        "verification",
        ],
    "settlements": [
        "definition",
        "create_settlement",
        "remove_transfer",
        "fetch_settlement",
        "fund_settlement",
        "split_payout",
        "list_settlements",
        "list_settlement_funding_transfers",
        "list_settlement_transfers",
        ],
    "guide_tokenization_js": [
        "definition",
        "associate_token",
        ],
    "test_data_finix": [
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
        "update_webhook",
        "fetch_webhook",
        "list_webhooks",
        "sample_payloads",
        ],
    "fees": [
        "definition"
    ],
    'FAQS': [
        'definition',
    ],
    "dashboard_overview_finix": [
        "definition"
    ],
    "idempotent_requests": [
        "definition",
    ],
    "topics": [
        'definition'
    ],
    'tags': [
        'definition'
    ],
    'errors_payouts': [
        'definition'
    ]
}

# This is the order that the directories / guides will be concatinated
resource_ordering = [
    "topics",
    "api_endpoints",
    "guide_authentication",
    "dashboard_overview_finix",
    "errors_payouts",
    "idempotent_requests",
    "tags",
    "test_data_finix",
    "guide_general_overview_finix",
    "guide_getting_started",
    "guide_push_to_card",
    "guide_pull_from_card",
    # "guide_iframe",
    "guide_hosted_fields_payouts",
    "guide_mobile",
    "guide_tripos",
    "authorizations",
    "devices",
    "disputes",
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
    "errors_payouts",
    'FAQS',
    "dashboard_overview_finix",
    "tags",
    "test_data_finix",
    "guide_general_overview_finix",
    "guide_getting_started",
    "guide_push_to_card",
    "guide_pull_from_card",
    # "guide_iframe",
    "guide_hosted_fields_payouts",
    "guide_mobile",
    "guide_admin_overview",
    "guide_create_application",
    "applications",
    "authorizations",
    "disputes",
    'fee_profile_overview',
    'guide_application_fee_profiles',
    'guide_merchant_fee_profiles',
    'fee_profile',
    "identities",
    # # "identity_verifications",
    "merchants",
    "payment_instruments",
    "settlements",
    "transfers",
    # "users",
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
