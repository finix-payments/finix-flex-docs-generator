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

from helpers import formatted_response, format_json, format_curl_request_body,\
    format_php_request_body, random_business_name, random_last_name, random_first_name

def create_user(config_values, role):
    values = {
        "role": role
    }
    values = format_json(json.dumps(values))
    endpoint = config_values["staging_base_url"] + '/users'
    return formatted_response(endpoint, values, config_values['admin_encoded_auth'])


def create_app(config_values, application_owner_user_id, company):
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
    endpoint = config_values["staging_base_url"] + '/applications'
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
    endpoint = config_values["staging_base_url"] + '/applications/' + config_values["application"] + "/processors"
    return formatted_response(endpoint, values, config_values['admin_encoded_auth'])
#
# def associate_identity_verification_processor(config_values):
#     values = {
#         "default_merchant_profile_id": None,
#         "type": config_values["identity_verification_processor"],
#         "config": {
#             "key1" : "value-1",
#             "key2" : "value-2",
#             }
#     }
#     values = format_json(json.dumps(values))
#     endpoint = config_values["staging_base_url"] + '/applications/' + config_values["application"] + "/processors"
#     return formatted_response(endpoint, values, config_values['admin_encoded_auth'])

# def create_user_merchant_role(config_values, identity_id):
#     values = """
#     {}
#     """
#     endpoint = config_values["staging_base_url"] + '/identities/' + identity_id + '/users'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])

def create_user_partner_role(config_values):
    values = """
    {}
    """
    endpoint = config_values["staging_base_url"] + '/applications/' + config_values["application"] + '/users'
    return formatted_response(endpoint, values, config_values['admin_encoded_auth'])

def create_buyer_identity(config_values):


    company = random_business_name()
    values = {
        "tags": {
            "key": "value"
        },
        "entity": {
            "last_name": random_last_name(),
            "first_name": random_first_name(),
            "doing_business_as": random_first_name() + " " + random_last_name(),
            "business_name": random_first_name() + " " + random_last_name(),
            "email": "therock@gmail.com",
            "phone": "7145677613",
            "personal_address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94114"
            }
        }
    }

    values = format_json(json.dumps(values))

    endpoint = config_values['staging_base_url'] + '/identities'
    return formatted_response(endpoint, values, config_values['encoded_auth'])

# def create_merchant_identity(config_values, business_type):
#     company = random_business_name()
#     values = {
#         "tags": {
#             "key": "value"
#         },
#         "entity": {
#             "last_name": "Sunkhronos",
#             "phone": "1234567890",
#             "personal_address": {
#                 "city": "San Mateo",
#                 "country": "USA",
#                 "region": "CA",
#                 "line2": "Apartment 7",
#                 "line1": "741 Douglass St",
#                 "postal_code": "94114"
#             },
#             "business_name": company,
#             "business_address": {
#                 "city": "San Mateo",
#                 "country": "USA",
#                 "region": "CA",
#                 "line2": "Apartment 8",
#                 "line1": "741 Douglass St",
#                 "postal_code": "94114"
#             },
#             "tax_id": "5779",
#             "business_type": business_type,
#             "business_phone": "+1 (408) 756-4497",
#             "first_name": "dwayne",
#             "dob": {
#                 "year": 1978,
#                 "day": 27,
#                 "month": 6
#             },
#             "incorporation_date": {
#                 "year": 1978,
#                 "day": 27,
#                 "month": 6
#             },
#             "business_tax_id": "123456789",
#             "mcc": "0742",
#             "default_statement_descriptor": company,
#             "max_transaction_amount": 120000,
#             "annual_card_volume": 12000000,
#             "url": "www." + company + ".com",
#             "principal_percentage_ownership": 50,
#             "url": "www." + company.replace(" ", "") + ".com",
#             "doing_business_as": company,
#             "email": "user@example.org"
#         }
#     }
#
#     values = format_json(json.dumps(values))
#
#     endpoint = config_values['staging_base_url'] + '/identities'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])

# def update_identity(config_values, identity_id):
#     values = """
# 	  {
# 	    "tags": {
# 	      "key_2": "value_2"
# 	    },
# 	    "entity": {
# 	      "last_name": "Sunkhronos",
# 	      "phone": "0987654321",
# 	      "personal_address": {
# 	        "city": "San Mateo",
# 	        "country": "USA",
# 	        "region": "CA",
# 	        "line2": "Apartment 7",
# 	        "line1": "741 Douglass St",
# 	        "postal_code": "94114"
# 	      },
# 	      "business_name": "business inc",
# 	      "business_address": {
# 	        "city": "San Mateo",
# 	        "country": "USA",
# 	        "region": "CA",
# 	        "line2": "Apartment 8",
# 	        "line1": "741 Douglass St",
# 	        "postal_code": "94114"
# 	      },
# 	      "tax_id": "5779",
# 	      "business_type": "LIMITED_LIABILITY_COMPANY",
# 	      "business_phone": "+1 (408) 756-4497",
# 	      "first_name": "Jimmy",
# 	      "dob": {
# 	        "year": 1978,
# 	        "day": 27,
# 	        "month": 6
# 	      },
# 	      "business_tax_id": "123456789",
# 	      "doing_business_as": "doingBusinessAs",
# 	      "email": "user@example.org"
# 	    }
# 	  }
# 	"""
#     endpoint = config_values['staging_base_url'] + '/identities/' + identity_id
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
def provision_merchant(config_values, identity_id):
    values = """
	  {
	    "tags": {
	      "key_2": "value_2"
	    }
	  }
	"""
    # values = format_json(json.dumps({"processor": config_values["payment_processor"]}))
    endpoint = config_values['staging_base_url'] + '/identities/' + identity_id + '/merchants'
    return formatted_response(endpoint, values, config_values['encoded_auth'])
#
# def create_identity_verification(config_values, identity_id):
#     values = {
#         "processor": config_values["identity_verification_processor"],
#         "identity": None,
#         "instrument": None,
#         "merchant": None,
#         }
#     values = format_json(json.dumps(values))
#     endpoint = config_values['staging_base_url'] + '/identities/' + identity_id + '/verifications'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])

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
        "name": random_first_name() + " " + random_last_name(),
        "security_code": "112",
        "type": "PAYMENT_CARD"
    }
    values = format_json(json.dumps(values))
    endpoint = config_values['staging_base_url'] + '/payment_instruments'
    return formatted_response(endpoint, values, config_values['encoded_auth'])
#
# def associate_token(config_values, identity_id, token):
#     values = {
#         "identity": identity_id,
#         "type": "TOKEN",
#         "token": token,
#         }
#     values = format_json(json.dumps(values))
#
#     endpoint = config_values['staging_base_url'] + '/payment_instruments'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def create_token(config_values):
#     values = {
#         "expiration_year": 2020,
#         "number": "4242424242424242",
#         "expiration_month": 12,
#         "address": {
#             "city": "San Mateo",
#             "country": "USA",
#             "region": "CA",
#             "line2": "Apartment 7",
#             "line1": "741 Douglass St",
#             "postal_code": "94114"
#         },
#         "security_code": "112",
#         "type": "PAYMENT_CARD"
#     }
#     values = format_json(json.dumps(values))
#
#
#     endpoint = config_values['staging_base_url'] + "/applications/" + config_values["application"] + "/tokens"
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def create_bank_account(config_values, identity_id):
#
#     values = {
#         "currency": "USD",
#         "account_type": "SAVINGS",
#         "name": "Fran Lemke",
#         "bank_code": "123123123",
#         "country": "USA",
#         "type": "BANK_ACCOUNT",
#         "identity": identity_id,
#         "account_number": "123123123"
#     }
#     values = format_json(json.dumps(values))
#
#     endpoint = config_values['staging_base_url'] + '/payment_instruments'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])


def create_debit(config_values, merchant_id, card_id, amount):
    values =  {
        "currency": "USD",
        "source": card_id,
        "merchant_identity": merchant_id,
        "amount": amount,
        "fee": 15,
        "tags": {
            "ride_number": "21DFASJSAKAS",
            "payment_reason": "referral"
        },
    }

    values = format_json(json.dumps(values))
    endpoint = config_values['staging_base_url'] + '/transfers'
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
#     endpoint = config_values['staging_base_url'] + '/transfers'
#     request = Request(endpoint, data=values, headers=headers)
#     response_body = urlopen(request).read()
#     response_body = format_json(response_body)
#     response_id = json.loads(response_body)["id"]
#     return {'request_body': values,
#             'response_body': response_body,
#             'response_id': response_id }

#
# def create_refund(config_values, transfer_id):
#     values = """
# 	  {
# 	  "refund_amount" : 100
#   	}
# 	"""
#     endpoint = config_values['staging_base_url'] + '/transfers/' + transfer_id + '/reversals'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def create_webhook(config_values):
#     values = """
# 	            {
# 	            "url" : "http://requestb.in/vts8mpvt"
# 	            }
# 	        """
#     endpoint = config_values['staging_base_url'] + '/webhooks'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#

def create_settlement(config_values, identity_id):

    time.sleep(60)

    values = {
        "currency": "USD",
        "processor": config_values['payment_processor']
    }
    values = format_json(json.dumps(values))
    endpoint = config_values['staging_base_url'] + '/identities/' + identity_id + "/settlements"
    return formatted_response(endpoint, values, config_values['encoded_auth'])


# def fetch_settlement(config_values, settlement_id):
#
#     values = None
#     endpoint = config_values['staging_base_url'] + '/settlements/' + settlement_id
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def fetch_settlement_transfers(config_values, settlement_id):
#     values = None
#     headers = {
#         'Content-Type': 'application/vnd.json+api',
#         'Authorization': 'Basic ' + config_values['encoded_auth']
#     }
#     endpoint = config_values['staging_base_url'] + '/settlements/' + settlement_id + "/transfers"
#     request = Request(endpoint, data=values, headers=headers)
#     response_body = urlopen(request).read()
#     response_body = format_json(response_body)
#     return {'request_body': values,
#             'response_body': response_body}
#
#
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
    endpoint = config_values['staging_base_url'] + '/disputes/'
    request = Request(endpoint, headers=headers)

    response_body = urlopen(request).read()
    response_body = format_json(response_body)

    # first dispute in collection
    dispute_resource = json.loads(response_body)['_embedded']['disputes'][0]
    return {'request_body': None,
            'response_body': dispute_resource,
            'response_id': dispute_resource["id"]}

#
# def create_authorization(config_values, merchant_id, card_id):
#
#     values = {
#         "currency": "USD",
#         "source": card_id,
#         "processor": config_values["payment_processor"],
#         "merchant_identity": merchant_id,
#         "amount": 100
#     }
#
#     values = format_json(json.dumps(values))
#
#     endpoint = config_values['staging_base_url'] + '/authorizations'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def capture_authorization(config_values, auth_id):
#
#     values = {
#         "capture_amount": 100,
#         "fee": "10",
#         "statement_descriptor": "Bob's Burgers",
#         "void_me": None
#     }
#
#     values = format_json(json.dumps(values))
#
#     headers = {
#         'Content-Type': 'application/vnd.json+api',
#         'Authorization': 'Basic ' + config_values['encoded_auth']
#     }
#     endpoint = config_values['staging_base_url'] + '/authorizations/' + auth_id
#     request = Request(endpoint, data=values, headers=headers)
#     request.get_method = lambda: 'PUT'
#     response_body = urlopen(request).read()
#     response_body = format_json(response_body)
#     response_id = json.loads(response_body)["id"]
#     return {'request_body': values,
#             'curl_request_body': format_curl_request_body(values),
#             'php_request_body': format_php_request_body(values),
#             'response_body': response_body,
#             'response_id': response_id}
#
#
# def fetch_authorization(config_values, auth_id):
#     values = None
#     endpoint = config_values['staging_base_url'] + '/authorizations/' + auth_id
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def fetch_dispute(config_values, dispute_id):
#
#     values = None
#
#     endpoint = config_values['staging_base_url'] + '/disputes/' + dispute_id
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def upload_dispute_file(config_values, dispute_id):
#
#     opener = poster.streaminghttp.register_openers()
#     values = {'file': open("testfile.txt", "rb"), 'name': 'file'}
#     datagen, headers = poster.encode.multipart_encode(values)
#
#     endpoint = config_values['staging_base_url'] + '/disputes/' + dispute_id + "/evidence"
#     request = Request(endpoint, datagen, headers)
#     request.add_header('Authorization', 'Basic %s' % config_values['encoded_auth'] ) # Add Auth header to request
#     response_body = urlopen(request).read()
#     response_body = format_json(response_body)
#     response_id = json.loads(response_body)["id"]
#     return {'request_body': values,
#             'response_body': response_body,
#             'response_id': response_id}
#
#
# def fetch_identity(config_values, identity_id):
#
#     values = None
#
#     endpoint = config_values['staging_base_url'] + '/identities/' + identity_id
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def fetch_merchant(config_values, merchant_id):
#
#     values = None
#
#     endpoint = config_values['staging_base_url'] + '/merchants/' + merchant_id
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def fetch_payment_instrument(config_values, instrument_id):
#
#     values = None
#
#     endpoint = config_values['staging_base_url'] + '/payment_instruments/' + instrument_id
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def fetch_identity_verification(config_values, verification_id):
#
#     values = None
#
#     endpoint = config_values['staging_base_url'] + '/verifications/' + verification_id
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def fetch_transfer(config_values, transfer_id):
#
#     values = None
#
#     endpoint = config_values['staging_base_url'] + '/transfers/' + transfer_id
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def fetch_webhook(config_values, webhook_id):
#
#     values = None
#
#     endpoint = config_values['staging_base_url'] + '/webhooks/' + webhook_id
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def list_authorizations(config_values):
#
#     values = None
#     endpoint = config_values['staging_base_url'] + '/authorizations'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def list_disputes(config_values):
#
#     values = None
#     endpoint = config_values['staging_base_url'] + '/disputes'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def list_identities(config_values):
#
#     values = None
#     endpoint = config_values['staging_base_url'] + '/identities'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def list_merchants(config_values):
#
#     values = None
#     endpoint = config_values['staging_base_url'] + '/merchants'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def list_payment_instruments(config_values):
#
#     values = None
#     endpoint = config_values['staging_base_url'] + '/payment_instruments'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def list_identity_verifications(config_values):
#
#     values = None
#     endpoint = config_values['staging_base_url'] + '/verifications'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def list_transfers(config_values):
#
#     values = None
#     endpoint = config_values['staging_base_url'] + '/transfers'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
#
# def list_webhooks(config_values):
#
#     values = None
#     endpoint = config_values['staging_base_url'] + '/webhooks'
#     return formatted_response(endpoint, values, config_values['encoded_auth'])
#
