import base64
from collections import OrderedDict

partner_configs = {
        'api_name': "CRB",
        'api_name_downcase': "crb",
        'admin_basic_auth_username': 'UShmqmxW5XUnAjWL8cTUYsp6',
        'admin_basic_auth_password': 'cf38541d-4ce2-43de-8414-a6cfade97d3d',
        'admin_encoded_auth': base64.b64encode('US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8'),
        'platform_basic_auth_username': 'UScDQHHFKkfFk5pLEGdn6zoK',
        'platform_basic_auth_password': '4c81c4dc-8f56-448a-9f6d-731a35e39e8f',
        'platform_encoded_auth': base64.b64encode('UScDQHHFKkfFk5pLEGdn6zoK:4c81c4dc-8f56-448a-9f6d-731a35e39e8f'),
        'basic_auth_username': None,
        'basic_auth_password': None,
        'encoded_auth': None,
        'basic_auth_username_payouts': None,
        'basic_auth_password_payouts': None,
        'encoded_auth_payouts': None,
        'payment_processor': "VISA_V1",
        'identity_verification_processor': "VISA_VA",
        'jsfiddle': "http://jsfiddle.net/rserna2010/2hxnjL0q/",
        'embedded_iframe_src': "https://vgs-assets.s3.amazonaws.com/payline-1.latest.js",
        'embedded_iframe_jsfiddle': "https://jsfiddle.net/ne96gvxs/",
        'staging_base_url': "https://api-staging.crbpay.io",
        'production_base_url': "https://api.crbpay.io",
        'python_client_resource_name': "CRB",
        'php_client_repo': "https://github.com/finix-payments/processing-php-client",
        'php_client_resource_name': "CRB",
        'python_client_resource_name': "crossriver",
        'php_client_repo': "https://github.com/finix-payments/processing-php-client",
        'ruby_client_resource_name': "CrossRiver",
        'ruby_gem': "finix",
        'ruby_require_statement': "finix",
        'java_artifact_id': "finix",
        'hosted_fields_src': "https://js.verygoodvault.com/js-vgfield-2/crb.js",
        'hosted_fields_jsfiddle': "https://jsfiddle.net/rserna2010/Ls101sou/",
}


# this provides the ordering for the docs by section and individual snippet
# Doc Type: [NON-ADMIN]
snippets_by_resource = {
    "api_endpoints":[
        "definition",
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
    "guide_general_overview_payouts": [
        "definition",
        ],
    "guide_iframe": [
        "definition",
        "associate_token",
    ],
    "guide_hosted_fields": [
        "definition",
        "associate_token",
    ],
    "guide_push_to_card": [
        "definition",
        "create_recipient_identity",
        "create_card",
        "verify_card",
        "provision_merchant_account",
        "send_to_recipient",
        ],
    "test_data": [
        "definition"
    ],
    "identities_payouts": [
        "definition",
        "create_recipient_identity",
        "fetch_identity",
        "list_identities",
        "update_identity",
        ],
    "payment_instruments_payouts": [
        "definition",
        "associate_token",
        "create_card",
        "fetch_credit_card",
        "verification"
        ],
    "guide_tokenization_js": [
        "definition",
        "associate_token",
        ],
    "payouts": [
        "definition",
        "create_payout",
        "fetch_transfer",
        "list_transfers",
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
        # "enable_dummy_processor",
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
    "guide_general_overview_payouts": [
        "definition",
        ],
    "guide_iframe": [
        "definition",
        "associate_token",
    ],
    "guide_hosted_fields": [
        "definition",
        "associate_token",
    ],
    "guide_push_to_card": [
        "definition",
        "create_recipient_identity",
        "create_card",
        "verify_card",
        "provision_merchant_account",
        "send_to_recipient",
        ],
    "test_data": [
        "definition"
    ],
    "identities_payouts": [
        "definition",
        "create_recipient_identity",
        "fetch_identity",
        "update_identity",
        "list_identities",
        ],
    "payment_instruments_payouts": [
        "definition",
        "associate_token",
        "create_card",
        "fetch_credit_card",
        "verification"
        ],
    "guide_tokenization_js": [
        "definition",
        "associate_token",
        ],
    "payouts": [
        "definition",
        "create_payout",
        "fetch_transfer",
        "list_transfers",
        ],
    }

# This is the order that the directories / guides will be concatinated
resource_ordering = [
    "guide_general_overview_payouts",
    "guide_authentication",
    "api_endpoints",
    "guide_push_to_card",
    "guide_iframe",
    "guide_hosted_fields",
    # "disputes",
    "identities_payouts",
    "payment_instruments_payouts",
    # "identity_verifications",
    "payouts",
]

admin_resource_ordering = [
    "guide_general_overview_payouts",
    "guide_authentication",
    "api_endpoints",
    "guide_push_to_card",
    "guide_iframe",
    "guide_hosted_fields",
    "test_data",
    "guide_admin_overview",
    "applications",
    # "disputes",
    "identities_payouts",
     # "identity_verifications",
    "payment_instruments_payouts",
    "payouts",
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
