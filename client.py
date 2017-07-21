import re
import string
import os
import base64
import json
import pprint
from urllib2 import Request, urlopen, HTTPError, URLError, build_opener, HTTPHandler
import poster
import time
import random

from helpers import formatted_response, format_json, format_curl_request_body, \
    format_php_request_body, random_business_name, random_last_name, \
    random_first_name, random_app_name, transfer_ready_to_settle, \
    stringified_elapsed_time, message_slack


class Client(object):
    staging_base_url = ""
    admin_basic_auth_username = ""
    admin_basic_auth_password = ""
    admin_basic_auth_username = ""
    platform_basic_auth_username = ""
    platform_basic_auth_password = ""
    basic_auth_username = ""
    basic_auth_password = ""
    basic_auth_username_payouts = ""
    basic_auth_password_payouts = ""


    def __init__(self,
                 staging_base_url = "",
                 admin_basic_auth_username = "",
                 admin_basic_auth_password = "",
                 platform_basic_auth_username = "",
                 platform_basic_auth_password = "",
                 basic_auth_username = "",
                 basic_auth_password = "",
                 basic_auth_username_payouts = "",
                 basic_auth_password_payouts = ""):
        # type: (object, object, object, object, object, object, object) -> object
        self.staging_base_url = staging_base_url
        self.admin_basic_auth_username = admin_basic_auth_username
        self.admin_basic_auth_password = admin_basic_auth_password
        self.admin_encoded_auth = base64.b64encode(self.admin_basic_auth_username + ':' + self.admin_basic_auth_password)

        self.platform_basic_auth_username = platform_basic_auth_username
        self.platform_basic_auth_password = platform_basic_auth_password
        self.platform_encoded_auth = base64.b64encode(self.platform_basic_auth_username + ':' + self.platform_basic_auth_password)

        self.basic_auth_username = basic_auth_username
        self.basic_auth_password = basic_auth_password
        self.encoded_auth = base64.b64encode(self.basic_auth_username + ':' + self.basic_auth_password)

        self.basic_auth_username_payouts = basic_auth_username_payouts
        self.basic_auth_password_payouts = basic_auth_password_payouts
        self.encoded_auth_payouts = base64.b64encode(self.basic_auth_username_payouts + ':' + self.basic_auth_password_payouts)

    def create_user(self, role):
        values = {
            "role": role
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/users'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def create_app(self, application_owner_user_id, business_type):
        company = random_app_name()

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
                "business_type": business_type,
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
                "max_transaction_amount": 1200000,
                "settlement_bank_account": "CORPORATE"
            }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/applications'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def associate_payment_processor(self, processor, application_id):
        if processor == "DUMMY_V1":
            values = {
                "type": processor,
                "config": {"key1": "value-1",
                           "key2": "value-2",
                           "canDebitBankAccount": True
                }
            }
        else:
            values = {
                "type": processor
            }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/applications/' + application_id + "/processors"
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def associate_identity_verification_processor(self, identity_verification_processor):
        values = {
            "default_merchant_profile_id": None,
            "type": identity_verification_processor,
            "config": {
                "key1" : "value-1",
                "key2" : "value-2",
                }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/applications/' + application_id + "/processors"
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def create_user_merchant_role(self, identity_id):
        values = """
        {}
        """
        endpoint = self.staging_base_url + '/identities/' + identity_id + '/users'
        return formatted_response(endpoint, values, self.encoded_auth)

    def create_user_partner_role(self, application_id):
        values = """
        {}
        """
        endpoint = self.staging_base_url + '/applications/' + application_id + '/users'
        return formatted_response(endpoint, values, self.platform_encoded_auth)


    def create_buyer_identity(self):
        values = {
            "tags": {
                "key": "value"
            },
            "entity": {
                "last_name": random_last_name(),
                "first_name": random_first_name(),
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

        endpoint = self.staging_base_url + '/identities'
        return formatted_response(endpoint, values, self.encoded_auth)


    def create_recipient_identity(self):
        first = random_first_name()
        values = {
            "tags": {
                "key": "value"
            },
            "entity": {
                "last_name": random_last_name(),
                "first_name": first,
                "email": first + "@gmail.com",
                "phone": "7145677612",
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

        endpoint = self.staging_base_url + '/identities'
        return formatted_response(endpoint, values, self.encoded_auth)


    def create_merchant_identity(self, business_type):
        if business_type == "TAX_EXEMPT_ORGANIZATION" or business_type == "GOVERNMENT_AGENCY":
            ownership_type = "PUBLIC"
        else:
            ownership_type = "PRIVATE"

        company = random_business_name()
        values = {
            "tags": {
                "Studio Rating": "4.7"
            },
            "entity": {
                "first_name": "dwayne",
                "last_name": "Sunkhronos",
                "title": "CEO",
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
                "tax_id": "123456789",
                "business_type": business_type,
                "business_phone": "+1 (408) 756-4497",
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
                "default_statement_descriptor": company,
                "max_transaction_amount": 12000000,
                "annual_card_volume": 12000000,
                "url": "www." + company + ".com",
                "has_accepted_credit_cards_previously": True,
                "principal_percentage_ownership": 50,
                "url": "www." + company.replace(" ", "") + ".com",
                "doing_business_as": company,
                "email": "user@example.org",
                "ownership_type": ownership_type
            }
        }

        values = format_json(json.dumps(values))

        endpoint = self.staging_base_url + '/identities'
        return formatted_response(endpoint, values, self.encoded_auth)

    def create_sender_identity(self, business_type):
        if business_type == "TAX_EXEMPT_ORGANIZATION" or business_type == "GOVERNMENT_AGENCY":
            ownership_type = "PUBLIC"
        else:
            ownership_type = "PRIVATE"

        company = random_business_name()
        values = {
            "processor": "VISA_V1",
            "tags": {
                "key_2": "value_2"
            }
        }

        values = format_json(json.dumps(values))

        endpoint = self.staging_base_url + '/identities'
        return formatted_response(endpoint, values, self.encoded_auth)

    def update_identity(self, identity_id):
        company = random_business_name()
        values = {
            "tags": {
                "key": "value_2"
            },
            "entity": {
                "first_name": "Bernard",
                "last_name": random_last_name(),
                "title": "CTO",
                "phone": "7144177878",
                "personal_address": {
                    "city": "San Diego",
                    "country": "USA",
                    "region": "CA",
                    "line2": "Apartment 2",
                    "line1": "712 Douglass St",
                    "postal_code": "94194"
                },
                "business_name": company,
                "personal_address": {
                    "city": "San Diego",
                    "country": "USA",
                    "region": "CA",
                    "line2": "Apartment 2",
                    "line1": "712 Douglass St",
                    "postal_code": "94194"
                },
                "tax_id": "999999999",
                "business_phone": "+1 (408) 756-4497",
                "dob": {
                    "year": 1988,
                    "day": 2,
                    "month": 5
                },
                "dob": {
                    "year": 1988,
                    "day": 2,
                    "month": 5
                },
                "business_tax_id": "123456789",
                "mcc": "0742",
                "default_statement_descriptor": company,
                "max_transaction_amount": 12000000,
                "max_transaction_amount": 1200000,
                "annual_card_volume": 12000000,
                "url": "www." + company + ".com",
                "has_accepted_credit_cards_previously": True,
                "principal_percentage_ownership": 50,
                "url": "www." + company.replace(" ", "") + ".com",
                "doing_business_as": company,
                "email": "user@example.org",
                "ownership_type": "PRIVATE"
            }
        }

        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/identities/' + identity_id
        return formatted_response(endpoint, values, self.encoded_auth, "PUT")

    def update_identity_payouts(self, identity_id):
        company = random_business_name()
        values = {
            "tags": {
                "key": "value"
            },
            "entity": {
                "last_name": random_last_name(),
                "first_name": random_first_name(),
                "email": random_first_name() + "@gmail.com",
                "phone": "7145677612",
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
        endpoint = self.staging_base_url + '/identities/' + identity_id
        return formatted_response(endpoint, values, self.encoded_auth, "PUT")


    def provision_merchant(self, identity_id, processor=None):
        values = {
            "tags": {
              "key_2": "value_2"
            },
            "processor": processor
          }

        values = format_json(json.dumps(values))

        endpoint = self.staging_base_url + '/identities/' + identity_id + '/merchants'
        return formatted_response(endpoint, values, self.encoded_auth)

    def provision_sender(self, identity_id, processor):
        values = {
            "tags": {
              "key_2": "value_2"
            },
            "processor": processor
          }

        values = format_json(json.dumps(values))

        endpoint = self.staging_base_url + '/identities/' + identity_id + '/merchants'
        return formatted_response(endpoint, values, self.encoded_auth)

    def create_identity_verification(self, identity_id, identity_verification_processor):
        values = {
            "processor": identity_verification_processor,
            "identity": None,
            "instrument": None,
            "merchant": None,
            }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/identities/' + identity_id + '/verifications'
        return formatted_response(endpoint, values, self.encoded_auth)

    def create_card(self, identity_id):
        values = {
            "identity": identity_id,
            "expiration_year": 2020,
            "number": "4957030420210454",
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
            "type": "PAYMENT_CARD",
            "tags": {
            "card_name": "Business Card"
            }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/payment_instruments'
        return formatted_response(endpoint, values, self.encoded_auth)

    def update_payment_instrument(self, payment_instrument_id):
        values = {
            "tags": {
                "order_number": "12121212"
            }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/payment_instruments/' + payment_instrument_id
        return formatted_response(endpoint, values, self.encoded_auth, "PUT")

    def update_transfer_tag(self, transfer_id):
        values = {
            "tags": {
                "Display Name": "Updated Field"
            }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/transfers/' + transfer_id
        return formatted_response(endpoint, values, self.encoded_auth, "PUT")

    def verify_payment_instrument(self, payment_instrument_id):
        values = {
        "processor": "VISA_V1"
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/payment_instruments/' + payment_instrument_id +'/verifications'
        return formatted_response(endpoint, values, self.encoded_auth)

    def check_card_updater(self, merchant_id, payment_instrument_id):
        values = {
            "merchant": merchant_id
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/payment_instruments/' + payment_instrument_id + '/updates'
        return formatted_response(endpoint, values, self.encoded_auth, "POST")


    def disable_user(self, user_id, toggle_boolean):
        values = {
            "enabled": toggle_boolean
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/users/' + user_id
        return formatted_response(endpoint, values, self.platform_encoded_auth, "PUT")

    def fund_settlement(self, settlement_id, bank_account_id):
        values = {
            "destination": bank_account_id
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/settlements/' + settlement_id
        return formatted_response(endpoint, values, self.platform_encoded_auth, "PUT")

    def toggle_merchant_processing(self, id, toggle_boolean):
        values = {
            "processing_enabled": toggle_boolean
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/merchants/' + id
        return formatted_response(endpoint, values, self.platform_encoded_auth, "PUT")

    def toggle_merchant_settlements(self, id, toggle_boolean):
        values = {
            "settlement_enabled": toggle_boolean
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/merchants/' + id
        return formatted_response(endpoint, values, self.platform_encoded_auth, "PUT")

    def toggle_application_processing(self, id, toggle_boolean):
        values = {
            "processing_enabled": toggle_boolean
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/applications/' + id
        return formatted_response(endpoint, values, self.platform_encoded_auth, "PUT")

    def toggle_application_settlements(self, id, toggle_boolean):
        values = {
            "settlement_enabled": toggle_boolean
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/applications/' + id
        return formatted_response(endpoint, values, self.platform_encoded_auth, "PUT")



    def associate_token(self, identity_id, token):
        values = {
            "identity": identity_id,
            "type": "TOKEN",
            "token": token,
            }
        values = format_json(json.dumps(values))

        endpoint = self.staging_base_url + '/payment_instruments'
        return formatted_response(endpoint, values, self.encoded_auth)


    def create_token(self, application_id):
        values = {
            "expiration_year": 2020,
            "number": "4957030420210454",
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


        endpoint = self.staging_base_url + "/applications/" + application_id + "/tokens"
        return formatted_response(endpoint, values, self.encoded_auth)


    def create_bank_account(self, identity_id):

        values = {
            "account_type": "SAVINGS",
            "name": "Fran Lemke",
            "bank_code": "123123123",
            "country": "USA",
            "type": "BANK_ACCOUNT",
            "identity": identity_id,
            "account_number": "123123123",
            "tags": {
                "Bank Account": "Company Account"
            }
        }
        values = format_json(json.dumps(values))

        endpoint = self.staging_base_url + '/payment_instruments'
        return formatted_response(endpoint, values, self.encoded_auth)


    def create_debit(self, merchant_id, card_id, amount):
        fee = int(round(amount * .1))
        values =  {
            "currency": "USD",
            "source": card_id,
            "merchant_identity": merchant_id,
            "amount": amount,
            "fee": fee,
            "tags": {
                "order_number": "21DFASJSAKAS"
            },
        }

        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/transfers'
        return formatted_response(endpoint, values, self.encoded_auth)

    def create_push_to_card_transfer(self, recipient_identity_id, card_id, amount):
        fee = int(round(amount * .1))
        values =  {
            "currency": "USD",
            "destination": card_id,
            "amount": amount,
            "tags": {
                "order_number": "21DFASJSAKAS"
                },
        }

        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/transfers'
        return formatted_response(endpoint, values, self.encoded_auth)

    # no longer allowing bank credits
    # def create_credit(self, merchant_id, bank_account_id):
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
    #         'Authorization': 'Basic ' + self.encoded_auth
    #     }
    #     endpoint = self.staging_base_url + '/transfers'
    #     request = Request(endpoint, data=values, headers=headers)
    #     response_body = urlopen(request).read()
    #     response_body = format_json(response_body)
    #     response_id = json.loads(response_body)["id"]
    #     return {'request_body': values,
    #             'response_body': response_body,
    #             'response_id': response_id }


    def create_refund(self, transfer_id):
        values = """
          {
          "refund_amount" : 100
        }
        """
        endpoint = self.staging_base_url + '/transfers/' + transfer_id + '/reversals'
        return formatted_response(endpoint, values, self.encoded_auth)


    def reattempt_provision_merchant(self, id):
        values = """
          {}
        """
        endpoint = self.staging_base_url + '/merchants/' + id + '/verifications'
        return formatted_response(endpoint, values, self.encoded_auth)


    def create_webhook(self):
        values = """
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                """
        endpoint = self.staging_base_url + '/webhooks'
        return formatted_response(endpoint, values, self.encoded_auth)


    def create_settlement(self, identity_id, transfer_id):
        # transfer_id is the ID of a recently created debit transfer. Here we're
        # checking  to see if its ready to settle, typically waiting period
        # should be 3600 milliseconds before
        # field changes
        start = time.time()
        minutes = 5
        endpoint = self.staging_base_url + '/transfers/' + transfer_id
        while not transfer_ready_to_settle(endpoint, self.encoded_auth):
            elapsed_time = time.time() - start
            if (elapsed_time // 60) % minutes == 0 and elapsed_time > 60:
                transfer_response = self.fetch_transfer(transfer_id)
                minutes = minutes + 20
                counter = stringified_elapsed_time(start)
                channel = '#fnx-dev'
                # This is the full response body
                # message = '*Transfer Reconciliation Latency Alert*\nElapsed Time: ' + counter + '\nEnvironment: ' + self.staging_base_url + '\n```' + transfer_response['response_body'] + '```'
                message = '*Transfer Reconciliation Latency Alert* (Exp 3mins)\nElapsed Time: ' + counter + '\nEnvironment: ' + self.staging_base_url + '\nTransfer ID: `' + transfer_response['response_id'] + '`'
                # message_slack(channel, message)
        values = {
            "currency": "USD",
            "tags": {
                "Internal Daily Settlement ID": "21DFASJSAKAS"
            }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/identities/' + identity_id + "/settlements"
        return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_settlement(self, settlement_id):

        values = None
        endpoint = self.staging_base_url + '/settlements/' + settlement_id
        return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_settlement_transfers(self, settlement_id):
        values = None
        headers = {
            'Content-Type': 'application/vnd.json+api',
            'Authorization': 'Basic ' + self.encoded_auth
        }
        endpoint = self.staging_base_url + '/settlements/' + settlement_id + "/transfers"
        request = Request(endpoint, data=values, headers=headers)
        response_body = urlopen(request).read()
        response_body = format_json(response_body)
        return {'request_body': values,
                'response_body': response_body}


    def create_dispute(self, merchant_id, card_id):

        # create dispute by debiting card with amount 888888
        debit = create_debit(self, merchant_id, card_id, 888888)

        # sleeping so that the dispute can be created
        time.sleep(240)
        # fetch list of all disputes
        headers = {
            'Content-Type': 'application/vnd.json+api',
            'Authorization': 'Basic ' + self.encoded_auth
        }
        # hit disputes index until transfers have a dispute link
        endpoint = self.staging_base_url + '/disputes/'
        request = Request(endpoint, headers=headers)

        response_body = urlopen(request).read()
        response_body = format_json(response_body)

        # first dispute in collection
        dispute_resource = json.loads(response_body)['_embedded']['disputes'][0]
        return {'request_body': None,
                'response_body': dispute_resource,
                'response_id': dispute_resource["id"]}


    def create_authorization(self, merchant_id, card_id):

        values = {
            "currency": "USD",
            "source": card_id,
            "merchant_identity": merchant_id,
            "amount": 100,
            "tags": {
                "order_number": "21DFASJSAKAS"
            }
            }

        values = format_json(json.dumps(values))

        endpoint = self.staging_base_url + '/authorizations'
        return formatted_response(endpoint, values, self.encoded_auth)


    def capture_authorization(self, auth_id):

        values = {
            "capture_amount": 100,
            "fee": "10"
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/authorizations/' + auth_id
        return formatted_response(endpoint, values, self.encoded_auth, "PUT")

    def void_authorization(self, auth_id):

        values = {
            "void_me": True,
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/authorizations/' + auth_id
        return formatted_response(endpoint, values, self.encoded_auth, "PUT")


    def fetch_authorization(self, auth_id):
        values = None
        endpoint = self.staging_base_url + '/authorizations/' + auth_id
        return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_dispute(self, dispute_id):

        values = None

        endpoint = self.staging_base_url + '/disputes/' + dispute_id
        return formatted_response(endpoint, values, self.encoded_auth)

    def fetch_user(self, id):
        values = None
        endpoint = self.staging_base_url + '/users/' + id
        return formatted_response(endpoint, values, self.encoded_auth)

    def fetch_application(self, id):
        values = None
        endpoint = self.staging_base_url + '/applications/' + id
        return formatted_response(endpoint, values, self.encoded_auth)

    def fetch_identity(self, id):
        values = None
        endpoint = self.staging_base_url + '/identities/' + id
        return formatted_response(endpoint, values, self.encoded_auth)

    def fetch_user(self, id):
        values = None
        endpoint = self.staging_base_url + '/users/' + id
        return formatted_response(endpoint, values, self.encoded_auth)

    def fetch_user(self, id):
        values = None
        endpoint = self.staging_base_url + '/users/' + id
        return formatted_response(endpoint, values, self.encoded_auth)

    def upload_dispute_file(self, dispute_id):

        opener = poster.streaminghttp.register_openers()
        values = {'file': open("testfile.txt", "rb"), 'name': 'file'}
        datagen, headers = poster.encode.multipart_encode(values)

        endpoint = self.staging_base_url + '/disputes/' + dispute_id + "/evidence"
        request = Request(endpoint, datagen, headers)
        request.add_header('Authorization', 'Basic %s' % self.encoded_auth ) # Add Auth header to request
        response_body = urlopen(request).read()
        response_body = format_json(response_body)
        response_id = json.loads(response_body)["id"]
        return {'request_body': values,
                'response_body': response_body,
                'response_id': response_id}


    def fetch_merchant(self, merchant_id):

        values = None

        endpoint = self.staging_base_url + '/merchants/' + merchant_id
        return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_bank_account(self, instrument_id):

        values = None

        endpoint = self.staging_base_url + '/payment_instruments/' + instrument_id
        return formatted_response(endpoint, values, self.encoded_auth)

    def fetch_credit_card(self, instrument_id):

        values = None

        endpoint = self.staging_base_url + '/payment_instruments/' + instrument_id
        return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_identity_verification(self, verification_id):

        values = None

        endpoint = self.staging_base_url + '/verifications/' + verification_id
        return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_transfer(self, transfer_id):

        values = None

        endpoint = self.staging_base_url + '/transfers/' + transfer_id
        return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_webhook(self, webhook_id):

        values = None

        endpoint = self.staging_base_url + '/webhooks/' + webhook_id
        return formatted_response(endpoint, values, self.encoded_auth)


    def list_authorizations(self):

        values = None
        endpoint = self.staging_base_url + '/authorizations'
        return formatted_response(endpoint, values, self.encoded_auth)


    def list_disputes(self):

        values = None
        endpoint = self.staging_base_url + '/disputes'
        return formatted_response(endpoint, values, self.encoded_auth)


    def list_identities(self):

        values = None
        endpoint = self.staging_base_url + '/identities'
        return formatted_response(endpoint, values, self.encoded_auth)


    def list_merchants(self):

        values = None
        endpoint = self.staging_base_url + '/merchants'
        return formatted_response(endpoint, values, self.encoded_auth)

    def list_merchant_verifications_platform_user(self, id):
        values = None
        endpoint = self.staging_base_url + '/merchants/' + id + '/verifications'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def list_merchant_verifications(self, id):
        values = None
        endpoint = self.staging_base_url + '/merchants/' + id + '/verifications'
        return formatted_response(endpoint, values, self.encoded_auth)


    def list_payment_instruments(self):
        values = None
        endpoint = self.staging_base_url + '/payment_instruments'
        return formatted_response(endpoint, values, self.encoded_auth)


    def list_identity_verifications(self):
        values = None
        endpoint = self.staging_base_url + '/verifications'
        return formatted_response(endpoint, values, self.encoded_auth)


    def list_transfers(self):
        values = None
        endpoint = self.staging_base_url + '/transfers'
        return formatted_response(endpoint, values, self.encoded_auth)

    def list_settlements(self):
        values = None
        endpoint = self.staging_base_url + '/settlements'
        return formatted_response(endpoint, values, self.encoded_auth)

    def list_settlement_transfers(self, id):
        values = None
        endpoint = self.staging_base_url + '/settlements/' + id + '/transfers'
        return formatted_response(endpoint, values, self.encoded_auth)

    def list_settlement_funding_transfers(self, id):
        values = None
        endpoint = self.staging_base_url + '/settlements/' + id + '/funding_transfers'
        return formatted_response(endpoint, values, self.encoded_auth)

    def list_applications(self):
        values = None
        endpoint = self.staging_base_url + '/applications/'
        return formatted_response(endpoint, values, self.encoded_auth)

    def list_users(self):
        values = None
        endpoint = self.staging_base_url + '/users/'
        return formatted_response(endpoint, values, self.encoded_auth)

    def list_webhooks(self):
        values = None
        endpoint = self.staging_base_url + '/webhooks'
        return formatted_response(endpoint, values, self.encoded_auth)
