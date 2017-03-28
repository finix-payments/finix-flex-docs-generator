import base64
from collections import OrderedDict

partner_configs = {
        'api_name': "CrossRiver",
        'api_name_downcase': "crossriver",
        'admin_basic_auth_username': 'US7AQLoX6FtZcPDttFAafEz2',
        'admin_basic_auth_password': 'f3276399-20f4-4bc3-aff0-71131cb347b8',
        'admin_encoded_auth': base64.b64encode('US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8'),
        'platform_basic_auth_username': 'US9C35Uh2qqqWLiaCHbMBb4c',
        'platform_basic_auth_password': 'a821faf7-625a-4ab8-943e-f5e8ef94b834',
        'platform_encoded_auth': base64.b64encode('US9C35Uh2qqqWLiaCHbMBb4c:a821faf7-625a-4ab8-943e-f5e8ef94b834'),
        'basic_auth_username': None,
        'basic_auth_password': None,
        'encoded_auth': None,
        'basic_auth_username_payouts': None,
        'basic_auth_password_payouts': None,
        'encoded_auth_payouts': None,
        'payment_processor': "DUMMY_V1",
        'identity_verification_processor': "DUMMY_V1",
        'jsfiddle': "http://jsfiddle.net/rserna2010/2hxnjL0q/",
        'embedded_iframe_src': "https://vgs-assets.s3.amazonaws.com/payline-1.latest.js",
        'embedded_iframe_jsfiddle': "https://jsfiddle.net/ne96gvxs/",
        'staging_base_url': "https://api-staging.finix.io",
        'production_base_url': "https://api.finix.io",
        'api_name_downcase': "crossriver",
        'python_client_resource_name': "crossriver",
        'php_client_repo': "https://github.com/finix-payments/processing-php-client",
        'ruby_client_resource_name': "CrossRiver",
        'ruby_gem': "finix",
        'ruby_require_statement': "finix",
        'java_artifact_id': "finix",
        'hosted_fields_src': "https://js.verygoodvault.com/js-vgfield-2/crb.js",
}


# this provides the ordering for the docs by section and individual snippet
# Doc Type: [NON-ADMIN]
snippets_by_resource = {
    "api_endpoints":[
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
    "disputes": [
        "definition",
        # "create_dispute",
        "fetch_dispute",
        "list_disputes",
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
    "guide_general_overview": [
        "definition",
        ],
    "guide_iframe": [
        "definition",
        "associate_token",
        ],
    "guide_push_to_card": [
        "definition",
        "create_recipient_identity",
        "create_card",
        "provision_merchant_account",
        "send_to_recipient",
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
    "payment_instruments": [
        "definition",
        "create_card",
        "associate_token",
        "fetch_credit_card",
        "update_payment_instrument",
        "list_payment_instruments",
        ],
    "guide_tokenization_js": [
        "definition",
        "associate_token",
        ],
    "payouts": [
        "definition",
        "create_debit",
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
        "list_users",
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
    "api_endpoints":[
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
    "disputes": [
        "definition",
        # "create_dispute",
        "fetch_dispute",
        "list_disputes",
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
    "guide_iframe": [
        "definition",
        "associate_token",
        ],
    "guide_push_to_card": [
        "definition",
        "create_recipient_identity",
        "create_card",
        "provision_merchant_account",
        "send_to_recipient",
        ],
    "test_data": [
        "definition"
    ],
    "identities": [
        "definition",
        "create_buyer_identity",
        "create_merchant_identity",
        "fetch_identity",
        "update_identity",
        "list_identities",
        ],
    "payment_instruments": [
        "definition",
        "associate_token",
        "create_card",
        "fetch_credit_card",
        "update_payment_instrument",
        "list_payment_instruments",
        ],
    "guide_tokenization_js": [
        "definition",
        "associate_token",
        ],
    "payouts": [
        "definition",
        "create_debit",
        "fetch_transfer",
        "create_refund",
        "list_transfers",
        ],
    "users": [
        "definition",
        "create_platform_user",
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
    "guide_authentication",
    "api_endpoints",
    "guide_push_to_card",
    "guide_iframe",
    "test_data",
    # "disputes",
    "identities",
    "payment_instruments",
    # "identity_verifications",
    "payouts",
    "webhooks",
]

admin_resource_ordering = [
    "guide_general_overview",
    "guide_authentication",
    "api_endpoints",
    "guide_push_to_card",
    "guide_iframe",
    "guide_tokenization_js",
    "test_data",
    "guide_admin_overview",
    "guide_create_application",
    "applications",
    # "disputes",
    "identities",
     # "identity_verifications",
    "payment_instruments",
    "payouts",
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
])

