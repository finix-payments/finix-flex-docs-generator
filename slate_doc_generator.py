import re
import string
import os
import base64
import json
import pprint
from urllib2 import Request, urlopen, HTTPError
import poster
import time
import random
import template_compiler
import client_compiler

class MyTemplate(string.Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
    '''

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
    {
        'api_name': "Payline",
        'api_name_downcase': "payline",
        'base_url': 'https://api-test.payline.io',
        'admin_basic_auth_username': 'USkoFNY73WEiP8tYmZtPa6e4',
        'admin_basic_auth_password': 'e28fe471-5b2c-4f20-9db9-0a3e5fd06110',
        'admin_encoded_auth': base64.b64encode('USkoFNY73WEiP8tYmZtPa6e4:e28fe471-5b2c-4f20-9db9-0a3e5fd06110'),
        'basic_auth_username': None,
        'basic_auth_password': None,
        'encoded_auth': None,
        'payment_processor': "DUMMY_V1",
        'identity_verification_processor': "DUMMY_V1",
        'application': None,
        'jsfiddle': "http://jsfiddle.net/rserna2010/sab76Lne/"
    },
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


def formatted_response(endpoint, values, encoded_auth):
    headers = {
        'Content-Type': 'application/vnd.json+api',
        'Authorization': 'Basic ' + encoded_auth
    }
    request = Request(endpoint, data=values, headers=headers)
    try:
        response_body = urlopen(request).read()
    except HTTPError as e:
        import ipdb; ipdb.set_trace()
        json.loads(e.read())
    response_body = format_json(response_body)
    response_id = json.loads(response_body)["id"]
    if values:
        return {'request_body': values,
                'curl_request_body': format_curl_request_body(values),
                'php_request_body': format_php_request_body(values),
                'response_body': response_body,
                'response_id': response_id}
    else:
        return {'request_body': values,
                'response_body': response_body,
                'response_id': response_id}



def format_json(response):
    response_body = json.loads(response)
    response_body = json.dumps(response_body, indent=4, sort_keys=False)
    response_body = response_body.replace("\n", "\n\t")
    if response_body[0] == "{":
        response_body = "\n\t" + response_body
    return response_body

def format_curl_request_body(string):
    return string.replace('"', '\\"')

def format_php_request_body(string):
    string = string.replace("{", "array(")
    string = string.replace("}", ")")
    string = string.replace(":", "=>")
    return string

def random_business_name():
    BusinessList = ["Bob's Burgers", "Jim's Bike Shop", "Gold's Gym", "Pete's Coffee",
                    "Pollos Hermanos", "Lee Sandwhiches", "Dunder Mifflin",
                    "Pawny City Hall", "ACME Anchors"]
    return random.choice (BusinessList)


def create_user(config_values, role):
    values = {
        "role": role
    }
    values = format_json(json.dumps(values))
    endpoint = config_values["base_url"] + '/users'
    return formatted_response(endpoint, values, config_values['admin_encoded_auth'])


def create_app(config_values, application_owner_user_id):
    company = random_business_name()
    values = {
        "tags": {
            "application_name": company
        },
        "user": application_owner_user_id,
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "tax_id": "5779",
            "business_type": "LIMITED_LIABILITY_COMPANY",
            "business_phone": "+1 (408) 756-4497",
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 5
            },
            "business_tax_id": "123456789",
            "doing_business_as": company,
            "email": "user@example.org",
            "max_transaction_amount": 12000,
            "settlement_bank_account": "CORPORATE"
        }
    }
    values = format_json(json.dumps(values))
    endpoint = config_values["base_url"] + '/applications'
    return formatted_response(endpoint, values, config_values['admin_encoded_auth'])


def associate_payment_processor(config_values):
    if config_values["payment_processor"] == "DUMMY_V1":
        values = {
            "default_merchant_profile_id": None,
            "type": config_values["identity_verification_processor"],
            "config": {
                "key1" : "value-1",
                "key2" : "value-2",
                }
        }
    else:
        values = {
            "default_merchant_profile_id": None,
            "type": config_values["payment_processor"],
            "config": {
                "sftpPort" : 22,
                "sftpUsername" : "finixtxn",
                "sftpPassword" : "u6Oq5O9S",
                "sftpTimeout" : 7200000,
                "payfacUsername" : "PAYLINEDATAMP",
                "payfacUrl" : "https://psp.litle.com/",
                "payfacPassword" : "gw9B33qL",
                "payfacMerchantId" : "07248611",
                "batchRequestFolder" : "/opt/processing/litle/requests",
                "timeout" : 10000,
                "batchUseSSL" : True,
                "proxyPort" : 1500,
                "reportGroup" : "Default Report Group",
                "allowPartialAuth" : False,
                "maxAllowedTransactionsPerFile" : 50000,
                "batchHost" : "payments.litle.com",
                "batchTcpTimeout" : 7200000,
                "proxyHost" : "",
                "maxTransactionsPerBatch" : 100000,
                "printxml" : True,
                "removeFetchedFile" : False,
                "batchResponseFolder" : "/opt/processing/litle/responses",
                "rateLimitTimeout" : 45000,
                "batchPort" : 22,
                "url" : "https://payments.litle.com/vap/communicator/online",
                "username" : "FINIX",
                "password" : "6DDu3bLm",
                "reportsSftpHost": "reports.litle.com",
                "reportsSftpUsername": "finixrpt",
                "reportsSftpPassword": "2By9Gm6O",
                "merchantFraudEnabled": False
            }
        }
    values = format_json(json.dumps(values))
    endpoint = config_values["base_url"] + '/applications/' + config_values["application"] + "/processors"
    return formatted_response(endpoint, values, config_values['admin_encoded_auth'])

def associate_identity_verification_processor(config_values):
    values = {
        "default_merchant_profile_id": None,
        "type": config_values["identity_verification_processor"],
        "config": {
            "key1" : "value-1",
            "key2" : "value-2",
            }
    }
    values = format_json(json.dumps(values))
    endpoint = config_values["base_url"] + '/applications/' + config_values["application"] + "/processors"
    return formatted_response(endpoint, values, config_values['admin_encoded_auth'])

def create_user_merchant_role(config_values, identity_id):
    values = """
    {}
    """
    endpoint = config_values["base_url"] + '/identities/' + identity_id + '/users'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_user_partner_role(config_values):
    values = """
    {}
    """
    endpoint = config_values["base_url"] + '/applications/' + config_values["application"] + '/users'
    return formatted_response(endpoint, values, config_values['admin_encoded_auth'])


def create_identity(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "tax_id": "5779",
            "business_type": "LIMITED_LIABILITY_COMPANY",
            "business_phone": "+1 (408) 756-4497",
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "mcc": "0742",
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "default_statement_descriptor": company,
            "principal_percentage_ownership": 50,
            "url": "www." + company.replace(" ", "") + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_buyer_identity(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Johnson",
            "first_name": "Dwayne",
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_scenario(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "tax_id": "5779",
            "business_type": "LIMITED_LIABILITY_COMPANY",
            "business_phone": "+1 (408) 756-4497",
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "mcc": "0742",
            "default_statement_descriptor": company,
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "url": "www." + company + ".com",
            "principal_percentage_ownership": 50,
            "url": "www." + company.replace(" ", "") + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def create_identity_individual_sole_proprietorship(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "tax_id": "5779",
            "default_statement_descriptor": company,
            "business_type": "INDIVIDUAL_SOLE_PROPRIETORSHIP",
            "principal_percentage_ownership": 100,
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_phone": "+1 (408) 756-4497",
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "mcc": "0742",
            "url": "www." + company + ".com",
            "doing_business_as": company,
            "url": "www." + company.replace(" ", "") + ".com",
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_corporation(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "tax_id": "5779",
            "default_statement_descriptor": company,
            "business_type": "CORPORATION",
            "business_phone": "+1 (408) 756-4497",
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "principal_percentage_ownership": 50,
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "mcc": "0742",
            "url": "www." + company + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_limited_liability_company(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "default_statement_descriptor": company,
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "tax_id": "5779",
            "business_type": "LIMITED_LIABILITY_COMPANY",
            "business_phone": "+1 (408) 756-4497",
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "default_statement_descriptor": company,
            "business_tax_id": "123456789",
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "principal_percentage_ownership": 50,
            "mcc": "0742",
            "url": "www." + company + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_partnership(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "default_statement_descriptor": company,
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "tax_id": "5779",
            "business_type": "PARTNERSHIP",
            "business_phone": "+1 (408) 756-4497",
            "principal_percentage_ownership": 50,
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "mcc": "0742",
            "url": "www." + company + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_limited_partnership(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "default_statement_descriptor": company,
            "tax_id": "5779",
            "business_type": "LIMITED_PARTNERSHIP",
            "business_phone": "+1 (408) 756-4497",
            "principal_percentage_ownership": 50,
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "mcc": "0742",
            "url": "www." + company + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_general_partnership(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "default_statement_descriptor": company,
            "tax_id": "5779",
            "business_type": "GENERAL_PARTNERSHIP",
            "business_phone": "+1 (408) 756-4497",
            "principal_percentage_ownership": 50,
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "mcc": "0742",
            "url": "www." + company + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_association_estate_trust(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "default_statement_descriptor": company,
            "tax_id": "5779",
            "business_type": "ASSOCIATION_ESTATE_TRUST",
            "business_phone": "+1 (408) 756-4497",
            "principal_percentage_ownership": 50,
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "mcc": "0742",
            "url": "www." + company + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_tax_exempt_organization(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "default_statement_descriptor": company,
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "tax_id": "5779",
            "business_type": "TAX_EXEMPT_ORGANIZATION",
            "business_phone": "+1 (408) 756-4497",
            "principal_percentage_ownership": 50,
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "mcc": "0742",
            "url": "www." + company + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_international_organization(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "default_statement_descriptor": company,
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "tax_id": "5779",
            "business_type": "INTERNATIONAL_ORGANIZATION",
            "business_phone": "+1 (408) 756-4497",
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "max_transaction_amount": 120000,
            "principal_percentage_ownership": 50,
            "annual_card_volume": 12000000,
            "mcc": "0742",
            "url": "www." + company + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_government_agency(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "principal_percentage_ownership": 50,
            "default_statement_descriptor": company,
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "tax_id": "5779",
            "business_type": "GOVERNMENT_AGENCY",
            "business_phone": "+1 (408) 756-4497",
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "mcc": "0742",
            "url": "www." + company + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_joint_venture(config_values):
    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": "Sunkhronos",
            "phone": "1234567890",
            "personal_address": {
                "city": "San Mateo",
                "principal_percentage_ownership": 50,
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "default_statement_descriptor": company,
            "business_name": company,
            "business_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 8",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            },
            "tax_id": "5779",
            "business_type": "JOINT_VENTURE",
            "business_phone": "+1 (408) 756-4497",
            "first_name": "dwayne",
            "dob": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "incorporation_date": {
                "year": 1978,
                "day": 27,
                "month": 6
            },
            "business_tax_id": "123456789",
            "max_transaction_amount": 120000,
            "annual_card_volume": 12000000,
            "mcc": "0742",
            "url": "www." + company + ".com",
            "doing_business_as": company,
            "email": "user@example.org"
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def update_identity(config_values, identity_id):
    values = """
	  {
	    "tags": {
	      "key_2": "value_2"
	    },
	    "entity": {
	      "last_name": "Sunkhronos",
	      "phone": "0987654321",
	      "personal_address": {
	        "city": "San Mateo",
	        "country": "USA",
	        "region": "CA",
	        "line2": "Apartment 7",
	        "line1": "741 Douglass St",
	        "postal_code": "94114"
	      },
	      "business_name": "business inc",
	      "business_address": {
	        "city": "San Mateo",
	        "country": "USA",
	        "region": "CA",
	        "line2": "Apartment 8",
	        "line1": "741 Douglass St",
	        "postal_code": "94114"
	      },
	      "tax_id": "5779",
	      "business_type": "LIMITED_LIABILITY_COMPANY",
	      "business_phone": "+1 (408) 756-4497",
	      "first_name": "Jimmy",
	      "dob": {
	        "year": 1978,
	        "day": 27,
	        "month": 6
	      },
	      "business_tax_id": "123456789",
	      "doing_business_as": "doingBusinessAs",
	      "email": "user@example.org"
	    }
	  }
	"""
    endpoint = config_values['base_url'] + '/identities/' + identity_id
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def underwrite_identity(config_values, identity_id):
    values = format_json(json.dumps({"processor": config_values["payment_processor"]}))
    endpoint = config_values['base_url'] + '/identities/' + identity_id + '/merchants'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_identity_verification(config_values, identity_id):
    values = {
        "processor": config_values["identity_verification_processor"],
        "identity": None,
        "instrument": None,
        "merchant": None,
        }
    values = format_json(json.dumps(values))
    endpoint = config_values['base_url'] + '/identities/' + identity_id + '/verifications'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_card(config_values, identity_id):
    values = {
        "identity": identity_id,
        "expiration_year": 2020,
        "number": "4242424242424242",
        "expiration_month": 12,
        "address": {
            "city": "San Mateo",
            "country": "USA",
            "region": "CA",
            "line2": "Apartment 7",
            "line1": "741 Douglass St",
            "postal_code": "94114"
        },
        "security_code": "112",
        "type": "PAYMENT_CARD"
    }
    values = format_json(json.dumps(values))
    endpoint = config_values['base_url'] + '/payment_instruments'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

def associate_token(config_values, identity_id, token):
    values = {
        "identity": identity_id,
        "type": "TOKEN",
        "token": token,
        }
    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/payment_instruments'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def create_token(config_values):
    values = {
        "expiration_year": 2020,
        "number": "4242424242424242",
        "expiration_month": 12,
        "address": {
            "city": "San Mateo",
            "country": "USA",
            "region": "CA",
            "line2": "Apartment 7",
            "line1": "741 Douglass St",
            "postal_code": "94114"
        },
        "security_code": "112",
        "type": "PAYMENT_CARD"
    }
    values = format_json(json.dumps(values))


    endpoint = config_values['base_url'] + "/applications/" + config_values["application"] + "/tokens"
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def create_bank_account(config_values, identity_id):

    values = {
        "currency": "USD",
        "account_type": "SAVINGS",
        "name": "Fran Lemke",
        "bank_code": "123123123",
        "country": "USA",
        "type": "BANK_ACCOUNT",
        "identity": identity_id,
        "account_number": "123123123"
    }
    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/payment_instruments'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def create_debit(config_values, merchant_id, card_id, amount):
    values =  {
        "currency": "USD",
        "source": card_id,
        "processor": config_values["payment_processor"],
        "merchant_identity": merchant_id,
        "amount": amount,
        "fee": 10
    }

    values = format_json(json.dumps(values))
    endpoint = config_values['base_url'] + '/transfers'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

# no longer allowing bank credits
# def create_credit(config_values, merchant_id, bank_account_id):
#     
#     values =  {
#         "currency" : "USD",
#         "destination": bank_account_id,
#         "processor": config_values["payment_processor"],
#         "merchant_identity": merchant_id,
#         "amount": 100,
#         "fee": 10,
#         }
#
#     values = format_json(json.dumps(values))
#
#     headers = {
#         'Content-Type': 'application/vnd.json+api',
#         'Authorization': 'Basic ' + config_values['encoded_auth']
#     }
#     endpoint = config_values['base_url'] + '/transfers'
#     request = Request(endpoint, data=values, headers=headers)
#     response_body = urlopen(request).read()
#     response_body = format_json(response_body)
#     response_id = json.loads(response_body)["id"]
#     return {'request_body': values,
#             'response_body': response_body,
#             'response_id': response_id }


def create_refund(config_values, transfer_id):
    values = """
	  {
	  "refund_amount" : 100
  	}		
	"""
    endpoint = config_values['base_url'] + '/transfers/' + transfer_id + '/reversals'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def create_webhook(config_values):
    values = """
	            {
	            "url" : "http://requestb.in/vts8mpvt"
	            }
	        """
    endpoint = config_values['base_url'] + '/webhooks'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def create_settlement(config_values, identity_id):

    time.sleep(60)

    values = {
        "processor": config_values['payment_processor'],
        "currency": "USD"
    }
    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/identities/' + identity_id + "/settlements"
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def fetch_settlement(config_values, settlement_id):

    values = None
    endpoint = config_values['base_url'] + '/settlements/' + settlement_id
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def fetch_settlement_transfers(config_values, settlement_id):
    values = None
    headers = {
        'Content-Type': 'application/vnd.json+api',
        'Authorization': 'Basic ' + config_values['encoded_auth']
    }
    endpoint = config_values['base_url'] + '/settlements/' + settlement_id + "/transfers"
    request = Request(endpoint, data=values, headers=headers)
    response_body = urlopen(request).read()
    response_body = format_json(response_body)
    return {'request_body': values,
            'response_body': response_body}


def create_dispute(config_values, merchant_id, card_id):

    # create dispute by debiting card with amount 888888
    debit = create_debit(config_values, merchant_id, card_id, 888888)

    time.sleep(90)
    # fetch list of all disputes
    headers = {
        'Content-Type': 'application/vnd.json+api',
        'Authorization': 'Basic ' + config_values['encoded_auth']
    }
    # hit disputes index until transfers have a dispute link
    endpoint = config_values['base_url'] + '/disputes/'
    request = Request(endpoint, headers=headers)

    response_body = urlopen(request).read()
    response_body = format_json(response_body)

    # first dispute in collection
    dispute_resource = json.loads(response_body)['_embedded']['disputes'][0]
    return {'request_body': None,
            'response_body': dispute_resource,
            'response_id': dispute_resource["id"]}


def create_authorization(config_values, merchant_id, card_id):

    values = {
        "currency": "USD",
        "source": card_id,
        "processor": config_values["payment_processor"],
        "merchant_identity": merchant_id,
        "amount": 100
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['base_url'] + '/authorizations'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def capture_authorization(config_values, auth_id):

    values = {
        "capture_amount": 100,
        "fee": "10",
        "statement_descriptor": "Bob's Burgers",
        "void_me": None
    }

    values = format_json(json.dumps(values))

    headers = {
        'Content-Type': 'application/vnd.json+api',
        'Authorization': 'Basic ' + config_values['encoded_auth']
    }
    endpoint = config_values['base_url'] + '/authorizations/' + auth_id
    request = Request(endpoint, data=values, headers=headers)
    request.get_method = lambda: 'PUT'
    response_body = urlopen(request).read()
    response_body = format_json(response_body)
    response_id = json.loads(response_body)["id"]
    return {'request_body': values,
            'curl_request_body': format_curl_request_body(values),
            'php_request_body': format_php_request_body(values),
            'response_body': response_body,
            'response_id': response_id}


def fetch_authorization(config_values, auth_id):
    values = None
    endpoint = config_values['base_url'] + '/authorizations/' + auth_id
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def fetch_dispute(config_values, dispute_id):

    values = None

    endpoint = config_values['base_url'] + '/disputes/' + dispute_id
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def upload_dispute_file(config_values, dispute_id):

    opener = poster.streaminghttp.register_openers()
    values = {'file': open("testfile.txt", "rb"), 'name': 'file'}
    datagen, headers = poster.encode.multipart_encode(values)

    endpoint = config_values['base_url'] + '/disputes/' + dispute_id + "/evidence"
    request = Request(endpoint, datagen, headers)
    request.add_header('Authorization', 'Basic %s' % config_values['encoded_auth'] ) # Add Auth header to request
    response_body = urlopen(request).read()
    response_body = format_json(response_body)
    response_id = json.loads(response_body)["id"]
    return {'request_body': values,
            'response_body': response_body,
            'response_id': response_id}


def fetch_identity(config_values, identity_id):

    values = None

    endpoint = config_values['base_url'] + '/identities/' + identity_id
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def fetch_merchant(config_values, merchant_id):

    values = None

    endpoint = config_values['base_url'] + '/merchants/' + merchant_id
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def fetch_payment_instrument(config_values, instrument_id):

    values = None

    endpoint = config_values['base_url'] + '/payment_instruments/' + instrument_id
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def fetch_identity_verification(config_values, verification_id):

    values = None

    endpoint = config_values['base_url'] + '/verifications/' + verification_id
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def fetch_transfer(config_values, transfer_id):

    values = None

    endpoint = config_values['base_url'] + '/transfers/' + transfer_id
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def fetch_webhook(config_values, webhook_id):

    values = None

    endpoint = config_values['base_url'] + '/webhooks/' + webhook_id
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def list_authorizations(config_values):

    values = None
    endpoint = config_values['base_url'] + '/authorizations'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def list_disputes(config_values):

    values = None
    endpoint = config_values['base_url'] + '/disputes'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def list_identities(config_values):

    values = None
    endpoint = config_values['base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def list_merchants(config_values):

    values = None
    endpoint = config_values['base_url'] + '/merchants'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def list_payment_instruments(config_values):

    values = None
    endpoint = config_values['base_url'] + '/payment_instruments'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def list_identity_verifications(config_values):

    values = None
    endpoint = config_values['base_url'] + '/verifications'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def list_transfers(config_values):

    values = None
    endpoint = config_values['base_url'] + '/transfers'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def list_webhooks(config_values):

    values = None
    endpoint = config_values['base_url'] + '/webhooks'
    return formatted_response(endpoint, values, config_values['encoded_auth'])


def generate_template_variables(config_values):

    ## create new user and app
    create_user_scenario = create_user(config_values, "ROLE_PARTNER")
    create_app_scenario = create_app(config_values, create_user_scenario["response_id"])
    config_values["application"] = create_app_scenario["response_id"]

    associate_payment_processor_scenario = associate_payment_processor(config_values)
    if config_values["payment_processor"] != "DUMMY_V1":
        associate_identity_verification_processor_scenario = associate_identity_verification_processor(config_values)
    create_user_partner_role_scenario = create_user_partner_role(config_values)
    config_values["basic_auth_username"] = create_user_scenario["response_id"]
    config_values["basic_auth_password"] = json.loads(create_user_scenario["response_body"])['password']
    config_values["encoded_auth"] = base64.b64encode(config_values["basic_auth_username"] + ':' + config_values["basic_auth_password"])


    # FIRST RUN SCENARIOS
    create_webhook_scenario = create_webhook(config_values)
    create_identity_scenario= create_identity(config_values)
    create_identity_individual_sole_proprietorship_scenario = create_identity_individual_sole_proprietorship(config_values)
    create_merchant_identity_scenario = create_identity_individual_sole_proprietorship_scenario
    create_identity_corporation_scenario = create_identity_corporation(config_values)
    create_identity_limited_liability_company_scenario = create_identity_limited_liability_company(config_values)
    create_identity_partnership_scenario = create_identity_partnership(config_values)
    create_identity_limited_partnership_scenario = create_identity_limited_partnership(config_values)
    create_identity_general_partnership_scenario = create_identity_general_partnership(config_values)
    create_identity_association_estate_trust_scenario = create_identity_association_estate_trust(config_values)
    create_identity_tax_exempt_organization_scenario = create_identity_tax_exempt_organization(config_values)
    create_identity_international_organization_scenario = create_identity_international_organization(config_values)
    create_identity_government_agency_scenario = create_identity_government_agency(config_values)
    # create_identity_joint_venture_scenario = create_identity_joint_venture(config_values)

    create_bank_account_scenario = create_bank_account(config_values, create_identity_scenario["response_id"])
    create_user_merchant_role_scenario = create_user_merchant_role(config_values, create_identity_scenario["response_id"])
    underwrite_identity_scenario = underwrite_identity(config_values, create_identity_scenario["response_id"])
    create_identity_verification_scenario = create_identity_verification(config_values, create_identity_scenario["response_id"])
    # create_credit_scenario = create_credit(config_values, create_identity_scenario["response_id"], create_bank_account_scenario["response_id"])

    create_buyer_identity_scenario = create_buyer_identity(config_values)
    create_card_scenario = create_card(config_values, create_buyer_identity_scenario["response_id"])
    create_debit_scenario = create_debit(config_values, create_identity_scenario['response_id'], create_card_scenario["response_id"], 100)
    create_dispute_scenario = create_dispute(config_values, create_identity_scenario['response_id'], create_card_scenario["response_id"])


    create_refund_scenario = create_refund(config_values, create_debit_scenario['response_id'])
    create_authorization_scenario = create_authorization(config_values, create_identity_scenario['response_id'], create_card_scenario["response_id"])
    capture_authorization_scenario = capture_authorization(config_values, create_authorization_scenario["response_id"])
    fetch_authorization_scenario = fetch_authorization(config_values, create_authorization_scenario["response_id"])
    create_settlement_scenario = create_settlement(config_values, create_identity_scenario['response_id'])
    create_token_scenario = create_token(config_values)
    associate_token_scenario = associate_token(config_values, create_identity_scenario["response_id"], create_token_scenario["response_id"])
    # update_identity_scenario = update_identity(config_values, create_identity_scenario["id"]


    # FETCH
    fetch_dispute_scenario = fetch_dispute(config_values, create_dispute_scenario["response_id"])
    fetch_identity_scenario = fetch_identity(config_values, create_identity_scenario["response_id"])
    fetch_merchant_scenario = fetch_merchant(config_values, underwrite_identity_scenario["response_id"])
    fetch_payment_instrument_scenario = fetch_payment_instrument(config_values, create_bank_account_scenario["response_id"])
    fetch_identity_verification_scenario = fetch_identity_verification(config_values, create_identity_verification_scenario["response_id"])
    fetch_transfer_scenario = fetch_transfer(config_values, create_debit_scenario["response_id"])
    fetch_webhook_scenario = fetch_webhook(config_values, create_webhook_scenario["response_id"])
    fetch_settlement_scenario = fetch_settlement(config_values, create_settlement_scenario['response_id'])
    fetch_settlement_transfers_scenario = fetch_settlement_transfers(config_values, create_settlement_scenario['response_id'])

    # LIST
    # list_authorizations_scenario = list_authorizations(config_values)
    # list_disputes_scenario = list_disputes(config_values)
    # list_identities_scenario = list_identities(config_values)
    # list_merchants_scenario = list_merchants(config_values)
    # list_payment_instruments_scenario = list_payment_instruments(config_values)
    # list_identity_verifications_scenario = list_identity_verifications(config_values)
    # list_transfers_scenario = list_transfers(config_values)
    # list_webhooks_scenario = list_webhooks(config_values)

    upload_dispute_file_scenario = upload_dispute_file(config_values, fetch_dispute_scenario["response_id"])
    # STORE RESULTS IN HASH FOR TEMPLATE
    api_scenario_vars = {
        # IDENTITIES --------------------------------------------

        "create_identity_scenario_curl_request": create_identity_scenario["curl_request_body"],
        "create_identity_scenario_php_request": create_identity_scenario["php_request_body"],
        "create_identity_scenario_response": create_identity_scenario["response_body"],
        "create_identity_scenario_id": create_identity_scenario["response_id"],


        "create_merchant_identity_scenario_curl_request": create_merchant_identity_scenario["curl_request_body"],
        "create_merchant_identity_scenario_php_request": create_merchant_identity_scenario["php_request_body"],
        "create_merchant_identity_scenario_response": create_merchant_identity_scenario["response_body"],
        "create_merchant_identity_scenario_id": create_merchant_identity_scenario["response_id"],


        "create_buyer_identity_scenario_curl_request": create_buyer_identity_scenario["curl_request_body"],
        "create_buyer_identity_scenario_php_request": create_buyer_identity_scenario["php_request_body"],
        "create_buyer_identity_scenario_response": create_buyer_identity_scenario["response_body"],
        "create_buyer_identity_scenario_id": create_buyer_identity_scenario["response_id"],

        "fetch_identity_scenario_request": fetch_identity_scenario["request_body"],
        "fetch_identity_scenario_response": fetch_identity_scenario["response_body"],
        "fetch_identity_scenario_id": fetch_identity_scenario["response_id"],


        # "list_identities_scenario_curl_request": list_identities_scenario["curl_request_body"],
        # "list_identities_scenario_php_request": list_identities_scenario["php_request_body"],
        # "list_identities_scenario_response": list_identities_scenario["response_body"],

        # MERCHANTS --------------------------------------------

        "underwrite_identity_scenario_curl_request": underwrite_identity_scenario["curl_request_body"],
        "underwrite_identity_scenario_php_request": underwrite_identity_scenario["php_request_body"],
        "underwrite_identity_scenario_response": underwrite_identity_scenario["response_body"],
        "underwrite_identity_scenario_id": underwrite_identity_scenario["response_id"],

        "fetch_merchant_scenario_request": fetch_merchant_scenario["request_body"],
        "fetch_merchant_scenario_response": fetch_merchant_scenario["response_body"],
        "fetch_merchant_scenario_id": fetch_merchant_scenario["response_id"],


        # "list_merchants_scenario_curl_request": list_merchants_scenario["curl_request_body"],
        # "list_merchants_scenario_php_request": list_merchants_scenario["php_request_body"],
        # "list_merchants_scenario_response": list_merchants_scenario["response_body"],


        # IDENTITY VERIFICATION --------------------------

        "create_identity_verification_scenario_curl_request": create_identity_verification_scenario["curl_request_body"],
        "create_identity_verification_scenario_php_request": create_identity_verification_scenario["php_request_body"],
        "create_identity_verification_scenario_response": create_identity_verification_scenario["response_body"],
        "create_identity_verification_scenario_id": create_identity_verification_scenario["response_id"],

        "fetch_identity_verification_scenario_request": fetch_identity_verification_scenario["request_body"],
        "fetch_identity_verification_scenario_response": fetch_identity_verification_scenario["response_body"],
        "fetch_identity_verification_scenario_id": fetch_identity_verification_scenario["response_id"],


        # "list_identity_verifications_scenario_curl_request": list_identity_verifications_scenario["curl_request_body"],
        # "list_identity_verifications_scenario_php_request": list_identity_verifications_scenario["php_request_body"],
        # "list_identity_verifications_scenario_response": list_identity_verifications_scenario["response_body"],

        # PAYMENT INSTRUMENTS (cards) --------------------------

        "create_card_scenario_curl_request": create_card_scenario["curl_request_body"],
        "create_card_scenario_php_request": create_card_scenario["php_request_body"],
        "create_card_scenario_response": create_card_scenario["response_body"],
        "create_card_scenario_id": create_card_scenario["response_id"],

        "fetch_payment_instrument_scenario_request": fetch_payment_instrument_scenario["request_body"],
        "fetch_payment_instrument_scenario_response": fetch_payment_instrument_scenario["response_body"],
        "fetch_payment_instrument_scenario_id": fetch_payment_instrument_scenario["response_id"],
        #

        # "list_payment_instruments_scenario_curl_request": list_payment_instruments_scenario["curl_request_body"],
        # "list_payment_instruments_scenario_php_request": list_payment_instruments_scenario["php_request_body"],
        # "list_payment_instruments_scenario_response": list_payment_instruments_scenario["response_body"],

        # PAYMENT INSTRUMENTS (bank accounts) --------------------------

        "create_bank_account_scenario_curl_request": create_bank_account_scenario["curl_request_body"],
        "create_bank_account_scenario_php_request": create_bank_account_scenario["php_request_body"],
        "create_bank_account_scenario_response": create_bank_account_scenario["response_body"],
        "create_bank_account_scenario_id": create_bank_account_scenario["response_id"],


        # TRANSFERS (Debits) --------------------------------------------

        "create_debit_scenario_curl_request": create_debit_scenario["curl_request_body"],
        "create_debit_scenario_php_request": create_debit_scenario["php_request_body"],
        "create_debit_scenario_response": create_debit_scenario["response_body"],
        "create_debit_scenario_id": create_debit_scenario["response_id"],

        "fetch_transfer_scenario_request": fetch_transfer_scenario["request_body"],
        "fetch_transfer_scenario_response": fetch_transfer_scenario["response_body"],
        "fetch_transfer_scenario_id": fetch_transfer_scenario["response_id"],


        # "list_transfers_scenario_curl_request": list_transfers_scenario["curl_request_body"],
        # "list_transfers_scenario_php_request": list_transfers_scenario["php_request_body"],
        # "list_transfers_scenario_response": list_transfers_scenario["response_body"],

        # # TRANSFERS (Credits) --------------------------------------------

        # "create_credit_scenario_curl_request": create_credit_scenario["curl_request_body"],
        # "create_credit_scenario_php_request": create_credit_scenario["php_request_body"],
        # "create_credit_scenario_response": create_credit_scenario["response_body"],
        # "create_credit_scenario_id": create_credit_scenario["response_id"],

        # TRANSFERS (Refunds) --------------------------------------------

        "create_refund_scenario_curl_request": create_refund_scenario["curl_request_body"],
        "create_refund_scenario_php_request": create_refund_scenario["php_request_body"],
        "create_refund_scenario_response": create_refund_scenario["response_body"],
        "create_refund_scenario_id": create_refund_scenario["response_id"],

        # AUTHORIZATIONS ------------------------------------------------------------

        "create_authorization_scenario_curl_request": create_authorization_scenario["curl_request_body"],
        "create_authorization_scenario_php_request": create_authorization_scenario["php_request_body"],
        "create_authorization_scenario_response": create_authorization_scenario["response_body"],
        "create_authorization_scenario_id": create_authorization_scenario["response_id"],


        "capture_authorization_scenario_curl_request": capture_authorization_scenario["curl_request_body"],
        "capture_authorization_scenario_php_request": capture_authorization_scenario["php_request_body"],
        "capture_authorization_scenario_response": capture_authorization_scenario["response_body"],
        "capture_authorization_scenario_id": capture_authorization_scenario["response_id"],

        "fetch_authorization_scenario_request": fetch_authorization_scenario["request_body"],
        "fetch_authorization_scenario_response": fetch_authorization_scenario["response_body"],
        "fetch_authorization_scenario_id": fetch_authorization_scenario["response_id"],


        # "list_authorizations_scenario_curl_request": list_authorizations_scenario["curl_request_body"],
        # "list_authorizations_scenario_php_request": list_authorizations_scenario["php_request_body"],
        # "list_authorizations_scenario_response": list_authorizations_scenario["response_body"],

        # DISPUTES ------------------------------------------------------------
        "create_dispute_scenario_request": create_dispute_scenario["request_body"],
        "create_dispute_scenario_response": create_dispute_scenario["response_body"],
        "create_dispute_scenario_id": create_dispute_scenario["response_id"],

        "fetch_dispute_scenario_request": fetch_dispute_scenario["request_body"],
        "fetch_dispute_scenario_response": fetch_dispute_scenario["response_body"],
        "fetch_dispute_scenario_id": fetch_dispute_scenario["response_id"],


        # "list_disputes_scenario_curl_request": list_disputes_scenario["curl_request_body"],
        # "list_disputes_scenario_php_request": list_disputes_scenario["php_request_body"],
        # "list_disputes_scenario_response": list_disputes_scenario["response_body"],

        # "upload_dispute_file_scenario_request": upload_dispute_file_scenario["request_body"]    ,
        # "upload_dispute_file_scenario_response": upload_dispute_file_scenario["response_body"],
        # "upload_dispute_file_scenario_id": upload_dispute_file_scenario["response_id"],

        # WEBHOOKS ------------------------------------------------------------

        "create_webhook_scenario_curl_request": create_webhook_scenario["curl_request_body"],
        "create_webhook_scenario_php_request": create_webhook_scenario["php_request_body"],
        "create_webhook_scenario_response": create_webhook_scenario["response_body"],
        "create_webhook_scenario_id": create_webhook_scenario["response_id"],

        "fetch_webhook_scenario_request": fetch_webhook_scenario["request_body"],
        "fetch_webhook_scenario_response": fetch_webhook_scenario["response_body"],
        "fetch_webhook_scenario_id": fetch_webhook_scenario["response_id"],


        # "list_webhooks_scenario_curl_request": list_webhooks_scenario["curl_request_body"],
        # "list_webhooks_scenario_php_request": list_webhooks_scenario["php_request_body"],

        # "list_webhooks_scenario_rcurl_esponse": list_webhooks_scenario["curl_request_body"],
        # "list_webhooks_scenario_rphp_esponse": list_webhooks_scenario["php_request_body"],

        # SETTLEMENTS -----------------------------------------------------

        "create_settlement_scenario_curl_request": create_settlement_scenario["curl_request_body"],
        "create_settlement_scenario_php_request": create_settlement_scenario["php_request_body"],
        "create_settlement_scenario_response": create_settlement_scenario["response_body"],
        "create_settlement_scenario_id": create_settlement_scenario["response_id"],

        "fetch_settlement_scenario_request": fetch_settlement_scenario["request_body"],
        "fetch_settlement_scenario_response": fetch_settlement_scenario["response_body"],
        "fetch_settlement_scenario_id": fetch_settlement_scenario["response_id"],
        #
        # "fetch_settlement_transfers_scenario_request": fetch_settlement_transfers_scenario["request_body"],
        # "fetch_settlement_transfers_scenario_response": fetch_settlement_transfers_scenario["response_body"],

        # APPLICATIONS -------------------------------------------------------
        "associate_payment_processor_scenario_request": associate_payment_processor_scenario["request_body"],
        "associate_payment_processor_scenario_response": associate_payment_processor_scenario["response_body"],
        "associate_payment_processor_scenario_id": associate_payment_processor_scenario["response_id"],

        "create_app_scenario_request": create_app_scenario["request_body"],
        "create_app_scenario_response": create_app_scenario["response_body"],
        "create_app_scenario_id": create_app_scenario["response_id"],

        # TOKENS -------------------------------------------------------
        "create_token_scenario_request": create_token_scenario["request_body"],
        "create_token_scenario_response": create_token_scenario["response_body"],
        "create_token_scenario_id": create_token_scenario["response_id"],



        "associate_token_scenario_curl_request": associate_token_scenario["curl_request_body"],
        "associate_token_scenario_php_request": associate_token_scenario["php_request_body"],
        "associate_token_scenario_response": associate_token_scenario["response_body"],
        "associate_token_scenario_id": associate_token_scenario["response_id"],

        # USERS --------------------------------------------
        "create_user_partner_role_scenario_request": create_user_partner_role_scenario["request_body"],
        "create_user_partner_role_scenario_response": create_user_partner_role_scenario["response_body"],
        "create_user_partner_role_scenario_id": create_user_partner_role_scenario["response_id"],
        "create_user_partner_role_scenario_password": json.loads(create_user_partner_role_scenario["response_body"])['password'],


        "create_user_merchant_role_scenario_request": create_user_merchant_role_scenario["request_body"],
        "create_user_merchant_role_scenario_response": create_user_merchant_role_scenario["response_body"],
        "create_user_merchant_role_scenario_id": create_user_merchant_role_scenario["response_id"],
        "create_user_merchant_role_scenario_password": json.loads(create_user_merchant_role_scenario["response_body"])['password']
    }

    # COMBINE CONFIGS W/ SCENARIO VARs
    template_vars = config_values.copy()
    template_vars.update(api_scenario_vars)
    return template_vars

# this generates a new version of the template
template_compiler.make_scenarios()

for api_configs in partner_configs:
    print "Building Docs for " + api_configs["api_name"]

    template_variables = generate_template_variables(api_configs)

    # open up template
    template = open('slate_template.md', 'r')
    data = template.read()
    t = MyTemplate(data)

    # create template for all
    file_name = os.getcwd() + "/rendered_slate_markdown/" + api_configs["api_name"] + ".html.md"
    print 'WRITING to: ' + file_name
    interpolated_file = t.substitute(template_variables)
    partner_doc_file = open(file_name, 'w')
    partner_doc_file.write(interpolated_file)


# this generates the PHP only template for running tests
client_compiler.make_scenarios()
snippet_directory_location = os.getcwd()
file = snippet_directory_location  + "/sections/client_header/php.md"
print 'WRITING to: ' + file
template = open(os.getcwd() + '/client_test_runner/php_test.md', 'r')
data = template.read()
t = MyTemplate(data)
interpolated_file = t.substitute(template_variables)
partner_doc_file = open(os.getcwd() + '/client_test_runner/php_test.php', 'w')
partner_doc_file.write(interpolated_file)
