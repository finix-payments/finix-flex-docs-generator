import base64
from collections import OrderedDict

partner_configs = {
        'api_name': "DC Bank",
        'api_name_downcase': "finix",
        'platform_basic_auth_username_payouts': 'US8HXXhg1hakavFEhNzpzLHk',
        'platform_basic_auth_password_payouts': '1bb1f91a-5e65-4667-bcb7-55d6fa1c0c79',
        'platform_encoded_auth_payouts': base64.b64encode('US8HXXhg1hakavFEhNzpzLHk:1bb1f91a-5e65-4667-bcb7-55d6fa1c0c79'),
        'basic_auth_username_payouts': None,
        'basic_auth_password_payouts': None,
        'encoded_auth_payouts': None,
        'payment_processor': "VISA_V1",
        'identity_verification_processor': "DUMMY_V1",
        'jsfiddle': "http://jsfiddle.net/rserna2010/2hxnjL0q/",
        'embedded_iframe_src': "https://forms.finixpymnts.com/finix.js",
        'embedded_iframe_jsfiddle': "https://jsfiddle.net/ne96gvxs/27/",
        'staging_base_url': "https://api-staging.finix.io",
        'production_base_url': "https://api.finix.io",
        'python_client_resource_name': "finix",
        'php_client_repo': "https://github.com/finix-payments/processing-php-client",
        'php_client_resource_name': "Finix",
        'ruby_client_resource_name': "Finix",
        'ruby_gem': "finix",
        'ruby_require_statement': "finix",
        'java_artifact_id': "finix",
        'version': '1.0.0',
        'java_group_id': "io.finix.payments.processing.client",
        'hosted_fields_src': "https://forms.finixpymnts.com/finix.js",
        'hosted_fields_jsfiddle': "https://jsfiddle.net/maserna2/znLe9kp6/",
        'ACH_business_day_delay': '3'
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
    "guide_hosted_fields_payouts": [
        "definition",
        "associate_token",
    ],
    # "guide_iframe": [
    #     "definition",
    #     "associate_token",
    # ],
    "guide_push_to_card": [
        "definition",
        "create_recipient_identity",
        "create_payment_card",
        "verify_card",
        "provision_merchant_account",
        "send_to_recipient",
        ],
    "test_data_payouts": [
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
        "create_payment_card",
        "fetch_payment_card",
        "verification"
        ],
    "guide_tokenization_js": [
        "definition",
        "associate_token_payouts",
        ],
    "payouts": [
        "definition",
        "create_payout",
        "fetch_transfer",
        "list_transfers",
        ],
    # "webhooks": [
    #     "definition",
    #     "create_webhook",
    #     "update_webhook",
    #     "fetch_webhook",
    #     "list_webhooks",
    #     "sample_payloads",
    #     ],
    "topics": [
    'definition',
    ],
    'test_data_visa': [
        'definition',
    ],
    'tags_payouts': [
        'definition',
    ],
    'errors': [
        'definition',
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
        # "disable_application_settlements",
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
    "guide_create_application_payouts": [
        "definition",
        "create_owner_user",
        "create_application",
        "enable_dummy_processor",
        "enable_processing",
        ],
    "guide_authentication": [
        "definition",
        "authentication",
        ],
    "guide_general_overview_payouts": [
        "definition",
        ],
    # "guide_iframe": [
    #     "definition",
    #     "associate_token",
    # ],
    "guide_hosted_fields_payouts": [
        "definition",
        "associate_token",
    ],
    "guide_push_to_card": [
        "definition",
        "create_recipient_identity",
        "create_payment_card",
        "verify_card",
        "provision_merchant_account",
        "send_to_recipient",
        ],
    "test_data_payouts": [
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
        "create_payment_card",
        "fetch_payment_card",
        "verification"
        ],
    "guide_tokenization_js": [
        "definition",
        "associate_token_payouts",
        ],
    "payouts": [
        "definition",
        "create_payout",
        "fetch_transfer",
        "list_transfers",
        ],
    # "webhooks": [
    #     "definition",
    #     "create_webhook",
    #     "update_webhook",
    #     "fetch_webhook",
    #     "list_webhooks",
    #     "sample_payloads",
    #     ],
    "topics": [
        'definition',
    ],
    'tags_payouts': [
        'definition',
    ],
    'test_data_payouts': [
        'definition',
    ],
    'errors': [
        'definition'
    ],
}

# This is the order that the directories / guides will be concatinated
resource_ordering = [
    "topics",
    "api_endpoints",
    "guide_authentication",
    "test_data_payouts",
    "tags_payouts",
    "errors",
    "guide_general_overview_payouts",
    "guide_push_to_card",
    # "guide_iframe",
    "guide_hosted_fields_payouts",
    # "disputes",
    "identities_payouts",
    "payment_instruments_payouts",
    # "identity_verifications",
    "payouts",
]

admin_resource_ordering = [
    "topics",
    "api_endpoints",
    "guide_authentication",
    "test_data_payouts",
    "tags_payouts",
    "errors",
    "guide_general_overview_payouts",
    "guide_create_application_payouts",
    "guide_authentication",
    "guide_push_to_card",
    # "guide_iframe",
    "guide_hosted_fields_payouts",
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
        ('Ruby', 'ruby'),
        ("PHP", "php"),
        ("Python", "python"),
])
