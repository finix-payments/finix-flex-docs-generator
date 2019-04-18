import base64
from collections import OrderedDict

partner_configs = {
        'api_name': "Peoples Payments",
        'api_name_downcase': "peoples payments",
        'platform_basic_auth_username_payouts': 'USh1oSjtQhxgmypHsbFsTKgb',
        'platform_basic_auth_password_payouts': '8af4a151-dd44-4658-bbb4-09a49c56132e',
        'platform_encoded_auth_payouts': base64.b64encode('USh1oSjtQhxgmypHsbFsTKgb:8af4a151-dd44-4658-bbb4-09a49c56132e'),
        'platform_basic_auth_username': 'USh1oSjtQhxgmypHsbFsTKgb',
        'platform_basic_auth_password': '8af4a151-dd44-4658-bbb4-09a49c56132e',
        'platform_encoded_auth': base64.b64encode('USh1oSjtQhxgmypHsbFsTKgb:8af4a151-dd44-4658-bbb4-09a49c56132e'),
        'basic_auth_username_payouts': None,
        'basic_auth_password_payouts': None,
        'encoded_auth_payouts': None,
        # 'payment_processor': "VISA_V1",
        # 'payment_processor': "LITLE_V1",
        'payment_processor': "DUMMY_V1",
        # 'payment_processor': "VANTIV_V1",
        'identity_verification_processor': "VISA_V1",
        'jsfiddle': "http://jsfiddle.net/rserna2010/2hxnjL0q/",
        'embedded_iframe_src': "https://forms.finixpymnts.com/finix.js",
        'embedded_iframe_jsfiddle': "https://jsfiddle.net/ne96gvxs/27/",
        'staging_base_url': "https://fastfunds-staging.peoplespayments.com",
        'production_base_url': "https://fastfunds.peoplespayments.com",
        'python_client_resource_name': "peoples_payments",
        'php_client_repo': "https://github.com/finix-payments/processing-php-client",
        'php_client_resource_name': "Finix",
        'ruby_client_resource_name': "PeoplesPayments",
        'ruby_gem': "PeoplesPayments",
        'ruby_require_statement': "PeoplesPayments",
        'java_artifact_id': "peoples-payments-java",
        'version': '1.1.0',
        'java_group_id': "io.github.peoples-payments",
        'hosted_fields_src': "https://forms.finixpymnts.com/peoplespayments.js",
        'hosted_fields_jsfiddle': "https://jsfiddle.net/maserna2/pzovjo6a",
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
        "create_batch_settlement",
        # "fund_settlement",
        # "refund_debit"
    ],
    "guide_iframe": [
        "definition",
        "associate_token",
    ],
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
        "create_payment_card",
        "create_bank_account",
        "associate_token",
        "fetch_bank_account",
        "fetch_payment_card",
        # "update_payment_instrument",
        "check_card_updater",
        "list_payment_instruments",
        # "verification",
        ],
    "settlements": [
        "definition",
        "create_settlement",
        "fetch_settlement",
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
    "guide_iframe": [
        "definition",
        "associate_token",
    ],
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
        "create_payment_card",
        "create_bank_account",
        "fetch_bank_account",
        "fetch_payment_card",
        # "update_payment_instrument",
        "check_card_updater",
        "list_payment_instruments",
        # "verification",
        ],
    "settlements": [
        "definition",
        "create_settlement",
        "remove_transfer",
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
    # "guide_push_to_card",
    "guide_iframe",
    "guide_hosted_fields_payouts",
    "guide_mobile",
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
    "errors_payouts",
    'FAQS',
    "dashboard_overview_finix",
    "tags",
    "test_data_finix",
    "guide_general_overview_finix",
    "guide_getting_started",
    # "guide_push_to_card",
    "guide_iframe",
    "guide_hosted_fields_payouts",
    "guide_mobile",
    "guide_admin_overview",
    "guide_create_application",
    "applications",
    "authorizations",
    # "disputes",
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
