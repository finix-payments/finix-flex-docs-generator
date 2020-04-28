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
import uuid

from helpers import formatted_response, format_json, format_curl_request_body, \
    format_php_request_body, random_business_name, random_last_name, \
    random_first_name, random_app_name, transfer_ready_to_settle, \
    stringified_elapsed_time


class Client(object):
    staging_base_url = ""
    # admin_basic_auth_username = ""
    # admin_basic_auth_password = ""
    platform_basic_auth_username = ""
    platform_basic_auth_password = ""
    platform_basic_auth_username_payouts = ""
    platform_basic_auth_password_payouts = ""
    basic_auth_username = ""
    basic_auth_password = ""
    basic_auth_username_payouts = ""
    basic_auth_password_payouts = ""


    def __init__(self,
                 staging_base_url = "",
                 # admin_basic_auth_username = "",
                 # admin_basic_auth_password = "",
                 platform_basic_auth_username = "",
                 platform_basic_auth_password = "",
                 platform_basic_auth_username_payouts = "",
                 platform_basic_auth_password_payouts = "",
                 basic_auth_username = "",
                 basic_auth_password = "",
                 basic_auth_username_payouts = "",
                 basic_auth_password_payouts = ""):
        # type: (object, object, object, object, object, object, object) -> object
        self.staging_base_url = staging_base_url
        # self.admin_basic_auth_username = admin_basic_auth_username
        # self.admin_basic_auth_password = admin_basic_auth_password
        # self.admin_encoded_auth = base64.b64encode(self.admin_basic_auth_username + ':' + self.admin_basic_auth_password)

        self.platform_basic_auth_username = platform_basic_auth_username
        self.platform_basic_auth_password = platform_basic_auth_password
        self.platform_encoded_auth = base64.b64encode(self.platform_basic_auth_username + ':' + self.platform_basic_auth_password)

        self.platform_basic_auth_username_payouts = platform_basic_auth_username_payouts
        self.platform_basic_auth_password_payouts = platform_basic_auth_password_payouts
        self.platform_encoded_auth_payouts = base64.b64encode(self.platform_basic_auth_username_payouts + ':' + self.platform_basic_auth_password_payouts)

        self.basic_auth_username = basic_auth_username
        self.basic_auth_password = basic_auth_password
        self.encoded_auth = base64.b64encode(self.basic_auth_username + ':' + self.basic_auth_password)

        self.basic_auth_username_payouts = basic_auth_username_payouts
        self.basic_auth_password_payouts = basic_auth_password_payouts
        self.encoded_auth_payouts = base64.b64encode(self.basic_auth_username_payouts + ':' + self.basic_auth_password_payouts)


    def create_user(self, role, product_type=None):
        values = {
            "role": role
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/users'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.platform_encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.platform_encoded_auth)

    def create_app(self, application_owner_user_id, business_type, product_type=None):
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
                "tax_id": "123456789",
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
                "max_transaction_amount": 1200000
            }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/applications'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.platform_encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.platform_encoded_auth)



    def associate_payment_processor(self, processor, application_id, product_type=None):
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
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.platform_encoded_auth_payouts)
        else:
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

    def create_user_merchant_role(self, identity_id, product_type=None):
        values = """
        {}
        """
        endpoint = self.staging_base_url + '/identities/' + identity_id + '/users'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)

    def create_user_partner_role(self, application_id, product_type=None):
        values = """
        {}
        """
        endpoint = self.staging_base_url + '/applications/' + application_id + '/users'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)


    def create_buyer_identity(self, product_type=None):
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
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)


    def create_recipient_identity(self, product_type=None):
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
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)

    def create_sender_identity(self, product_type=None):
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
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
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

    # def create_sender_identity(self, business_type):
    #     if business_type == "TAX_EXEMPT_ORGANIZATION" or business_type == "GOVERNMENT_AGENCY":
    #         ownership_type = "PUBLIC"
    #     else:
    #         ownership_type = "PRIVATE"
    #
    #     company = random_business_name()
    #     values = {
    #         "processor": "VISA_V1",
    #         "tags": {
    #             "key_2": "value_2"
    #         }
    #     }
    #
    #     values = format_json(json.dumps(values))
    #
    #     endpoint = self.staging_base_url + '/identities'
    #     return formatted_response(endpoint, values, self.encoded_auth)

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
        return formatted_response(endpoint, values, self.encoded_auth_payouts, "PUT")


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

    def provision_sender(self, identity_id, processor, product_type=None):
        values = {
            "processor": processor
          }

        values = format_json(json.dumps(values))

        endpoint = self.staging_base_url + '/identities/' + identity_id + '/merchants'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
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

    def create_card_canada(self, identity_id, card_number, currency, product_type=None):
        values = {
            "currency": currency,
            "identity": identity_id,
            "expiration_year": 2029,
            "number": card_number ,
            "expiration_month": 03,
            "address": {
                "city": "San Mateo",
                "country": "USA",
                "region": "CA",
                "line2": "Apartment 7",
                "line1": "741 Douglass St",
                "postal_code": "94404"
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
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)

    def create_card_verification(self, identity_id, product_type=None):
        values = {
            "identity": identity_id,
            "expiration_year": 2029,
            "number": "4815070000000018" ,
            "expiration_month": 03,
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
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)

    def create_card(self, identity_id, product_type=None):
        values = {
            "identity": identity_id,
            "expiration_year": 2029,
            "number": "4895142232120006" ,
            # "number": "4957030420210454" ,

            "expiration_month": 03,
            "address": {
                "city": "San Francisco",
                "country": "USA",
                "region": "CA",
                "line1": "900 Metro Center Blv",
                "postal_code": "94404"
            },
            "name": random_first_name() + " " + random_last_name(),
            "security_code": "022",
            "type": "PAYMENT_CARD",
            "tags": {
            "card_name": "Business Card"
            }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/payment_instruments'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)

    # def create_aft_card(self, identity_id, product_type=None):
    #     values = {
    #         "identity": identity_id,
    #         "expiration_year": 2020,
    #         "number": "4957030420210454",
    #         "expiration_month": 12,
    #         "address": {
    #             "city": "San Mateo",
    #             "country": "USA",
    #             "region": "CA",
    #             "line2": "Apartment 7",
    #             "line1": "741 Douglass St",
    #             "postal_code": "94114"
    #         },
    #         "name": random_first_name() + " " + random_last_name(),
    #         "security_code": "112",
    #         "type": "PAYMENT_CARD",
    #         "tags": {
    #         "card_name": "Business Card"
    #         }
    #     }
    #     values = format_json(json.dumps(values))
    #     endpoint = self.staging_base_url + '/payment_instruments'
    #     if(product_type == 'payouts'):
    #         return formatted_response(endpoint, values, self.encoded_auth_payouts)
    #     else:
    #         return formatted_response(endpoint, values, self.encoded_auth)


    def update_payment_instrument(self, payment_instrument_id):
        values = {
            "tags": {
                "Display Name": "Updated Field"
            }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/payment_instruments/' + payment_instrument_id
        return formatted_response(endpoint, values, self.encoded_auth, "PUT")

    def update_transfer(self, transfer_id):
        values = {
            "tags": {
                "order_number": "12121212"
            }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/transfers/' + transfer_id
        return formatted_response(endpoint, values, self.encoded_auth, "PUT")

    # def create_fee_profile(self, application_id, merchant=None ):
    #
    #     if(merchant == "merchant-tiered"):
    #         values = {
    #             "tags": {
    #                 "app pricing": "merchant-tiered"
    #             },
    #             'merchant': application_id,
    #             'basis_points': 200,
    #             'fixed_fee': 100,
    #             'ach_basis_points': 300,
    #             "ach_fixed_fee" : 30,
    #             'charge_interchange': False,
    #             "qualified_tiers": {
    #         		"AMERICAN_EXPRESS": {
    #         			"CREDIT": [{
    #         					"display_name": "Amex Credit Qualified",
    #         					"basis_points": 330,
    #         					"fixed": 70,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "INCLUSIVE",
    #         					"range_high": 175,
    #         					"range_low": 0
    #         				},
    #         				{
    #         					"display_name": "Amex Credit Mid-Qualified",
    #         					"basis_points": 440,
    #         					"fixed": 80,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 239,
    #         					"range_low": 175
    #         				},
    #         				{
    #         					"display_name": "Amex Credit Non-Qualified",
    #         					"basis_points": 550,
    #         					"fixed": 90,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 10000,
    #         					"range_low": 239
    #         				}
    #         			]
    #         		},
    #         		"DISCOVER": {
    #         			"CREDIT": [{
    #
    #         					"display_name": "Discover Credit Qualified",
    #         					"basis_points": 255,
    #         					"fixed": 30,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "INCLUSIVE",
    #         					"range_high": 175,
    #         					"range_low": 0
    #         				},
    #         				{
    #         					"display_name": "Discover Credit Mid-Qualified",
    #         					"basis_points": 325,
    #         					"fixed": 40,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 239,
    #         					"range_low": 175
    #         				},
    #         				{
    #         					"display_name": "Discover Credit Non-Qualified",
    #         					"basis_points": 375,
    #         					"fixed": 50,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 10000,
    #         					"range_low": 239
    #         				}
    #         			],
    #         			"DEBIT": [{
    #         					"display_name": "Discover Debit Qualified",
    #         					"basis_points": 225,
    #         					"fixed": 25,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "INCLUSIVE",
    #         					"range_high": 160,
    #         					"range_low": 0
    #         				},
    #         				{
    #         					"display_name": "Discover Debit Mid-Qualified",
    #         					"basis_points": 275,
    #         					"fixed": 35,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 200,
    #         					"range_low": 160
    #         				},
    #         				{
    #         					"display_name": "Discover Debit Non-Qualified",
    #         					"basis_points": 325,
    #         					"fixed": 40,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 10000,
    #         					"range_low": 200
    #         				}
    #         			]
    #         		},
    #         		"MASTERCARD": {
    #         			"CREDIT": [{
    #         					"display_name": "Mastercard Credit Qualified",
    #         					"basis_points": 255,
    #         					"fixed": 30,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "INCLUSIVE",
    #         					"range_high": 175,
    #         					"range_low": 0
    #         				},
    #         				{
    #         					"display_name": "Mastercard Credit Mid-Qualified",
    #         					"basis_points": 325,
    #         					"fixed": 40,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 239,
    #         					"range_low": 175
    #         				},
    #         				{
    #         					"display_name": "Mastercard Credit Non-Qualified",
    #         					"basis_points": 375,
    #         					"fixed": 50,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 10000,
    #         					"range_low": 239
    #         				}
    #         			],
    #         			"DEBIT": [{
    #         					"display_name": "Mastercard Debit Qualified",
    #         					"basis_points": 225,
    #         					"fixed": 25,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "INCLUSIVE",
    #         					"range_high": 160,
    #         					"range_low": 0
    #         				},
    #         				{
    #         					"display_name": "Mastercard Debit Mid-Qualified",
    #         					"basis_points": 275,
    #         					"fixed": 35,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "INCLUSIVE",
    #         					"range_high": 200,
    #         					"range_low": 160
    #         				},
    #         				{
    #         					"display_name": "Mastercard Debit Non-Qualified",
    #         					"basis_points": 325,
    #         					"fixed": 40,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 10000,
    #         					"range_low": 200
    #         				}
    #         			]
    #         		},
    #         		"VISA": {
    #         			"CREDIT": [{
    #         					"display_name": "Visa Credit Qualified",
    #         					"basis_points": 255,
    #         					"fixed": 30,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "INCLUSIVE",
    #         					"range_high": 175,
    #         					"range_low": 0
    #         				},
    #         				{
    #         					"display_name": "Visa Credit Mid-Qualified",
    #         					"basis_points": 325,
    #         					"fixed": 40,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 239,
    #         					"range_low": 175
    #         				},
    #         				{
    #         					"display_name": "Visa Credit Non-Qualified",
    #         					"basis_points": 375,
    #         					"fixed": 50,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 10000,
    #         					"range_low": 239
    #         				}
    #         			],
    #         			"DEBIT": [{
    #         					"display_name": "Visa Debit Qualified",
    #         					"basis_points": 225,
    #         					"fixed": 25,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "INCLUSIVE",
    #         					"range_high": 160,
    #         					"range_low": 0
    #         				},
    #         				{
    #         					"display_name": "Visa Debit Mid-Qualified",
    #         					"basis_points": 275,
    #         					"fixed": 35,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 200,
    #         					"range_low": 160
    #         				},
    #         				{
    #         					"display_name": "Visa Debit Non-Qualified",
    #         					"basis_points": 325,
    #         					"fixed": 40,
    #         					"high_type": "INCLUSIVE",
    #         					"low_type": "EXCLUSIVE",
    #         					"range_high": 10000,
    #         					"range_low": 200
    #                     				}
    #                     			]
    #                     		}
    #                     	}
    #                 }
    #     elif (merchant == "merchant"):
    #         values = {
    #             "tags": {
    #                 "app pricing": "merchant"
    #             },
    #             'merchant': application_id,
    #             'basis_points': 200,
    #             'fixed_fee': 100,
    #             'ach_basis_points': 300,
    #             "ach_fixed_fee" : 30,
    #             'charge_interchange': False
    #         }
    #     else:
    #         values = {
    #         "tags": {
    #             "app pricing": "application"
    #         },
    #             'application': application_id,
    #             'basis_points': 200,
    #             'fixed_fee': 100,
    #             'ach_basis_points': 300,
    #             "ach_fixed_fee" : 30,
    #             'charge_interchange': False
    #         }
    #
    #     values = format_json(json.dumps(values))
    #     endpoint = self.staging_base_url + '/fee_profiles'
    #     return formatted_response(endpoint, values, self.platform_encoded_auth, "POST")


    def create_fee_profile(self, application_id):
        values = {
            "tags": {
                "app pricing": "sample"
            },
            'application': application_id,
            'basis_points': 200,
            'fixed_fee': 100,
            'ach_basis_points': 300,
            "ach_fixed_fee" : 30,
            'charge_interchange': False
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/fee_profiles'
        return formatted_response(endpoint, values, self.platform_encoded_auth, "POST")


    def create_fee_profile_qualified_tiers(self, application_id):
        values = {
            "tags": {
                "app pricing": "sample"
            },
            'application': application_id,
            'basis_points': 200,
            'fixed_fee': 100,
            'ach_basis_points': 300,
            "ach_fixed_fee" : 30,
            'charge_interchange': False,
             "qualified_tiers": {
                "american_express": {
                    "credit": [
                        {
                            "display_name": "American Express Credit Qualified Rate",
                            "basis_points": 330,
                            "fixed": 70,
                            "max_interchange": 175
                        },
                        {
                        	"display_name": "American Express Credit Mid-Qualified Rate",
                            "basis_points": 440,
                            "fixed": 80,
                            "max_interchange": 239
                        },
                        {
                        	"display_name": "American Express Credit Non-Qualified Rate",
                            "basis_points": 550,
                            "fixed": 90
                        }
                    ]
                },
                "discover": {
                    "credit": [
                        {
                        	"display_name": "Discover Credit Qualified Rate",
                            "basis_points": 255,
                            "fixed": 30,
                            "max_interchange": 175
                        },
                        {
                        	"display_name": "Discover Credit Mid-Qualified Rate",
                            "basis_points": 325,
                            "fixed": 40,
                            "max_interchange": 239
                        },
                        {
                        	"display_name": "Discover Credit Non-Qualified Rate",
                            "basis_points": 375,
                            "fixed": 50
                        }
                    ],
                    "debit": [
                        {
                        	"display_name": "Discover Debit Qualified Rate",
                            "basis_points": 225,
                            "fixed": 25,
                            "max_interchange": 160
                        },
                        {
                        	"display_name": "Discover Debit Mid-Qualified Rate",
                            "basis_points": 275,
                            "fixed": 35,
                            "max_interchange": 200
                        },
                        {
                        	"display_name": "Discover Debit Non-Qualified Rate",
                            "basis_points": 325,
                            "fixed": 40
                        }
                    ]
                },
                "mastercard": {
                    "credit": [
                        {
                        	"display_name": "Mastercard Credit Qualified Rate",
                            "basis_points": 255,
                            "fixed": 30,
                            "max_interchange": 175
                        },
                        {
                        	"display_name": "Mastercard Credit Mid-Qualified Rate",
                            "basis_points": 325,
                            "fixed": 40,
                            "max_interchange": 239
                        },
                        {
                        	"display_name": "Mastercard Credit Non-Qualified Rate",
                            "basis_points": 375,
                            "fixed": 50
                        }
                    ],
                    "debit": [
                        {
                        	"display_name": "Mastercard Debit Qualified Rate",
                            "basis_points": 225,
                            "fixed": 25,
                            "max_interchange": 160
                        },
                        {
                        	"display_name": "Mastercard Debit Mid-Qualified Rate",
                            "basis_points": 275,
                            "fixed": 35,
                            "max_interchange": 200
                        },
                        {
                        	"display_name": "Mastercard Debit Non-Qualified Rate",
                            "basis_points": 325,
                            "fixed": 40
                        }
                    ]
                },
                "visa": {
                    "credit": [
                        {
                        	"display_name": "Visa Credit Qualified Rate",
                            "basis_points": 225,
                            "fixed": 30,
                            "max_interchange": 175
                        },
                        {
                        	"display_name": "Visa Credit Mid-Qualified Rate",
                            "basis_points": 325,
                            "fixed": 40,
                            "max_interchange": 239
                        },
                        {
                        	"display_name": "Visa Credit Non-Qualified Rate",
                            "basis_points": 375,
                            "fixed": 50
                        }
                    ],
                    "debit": [
                        {
                        	"display_name": "Visa Debit Qualified",
                            "basis_points": 225,
                            "fixed": 25,
                            "max_interchange": 160
                        },
                        {
                        	"display_name": "Visa Debit Mid-Qualified",
                            "basis_points": 275,
                            "fixed": 35,
                            "max_interchange": 200
                        },
                        {
                        	"display_name": "Visa Debit Non-Qualified",
                            "basis_points": 325,
                            "fixed": 40
                        }
                    ]
                },
                "unknown_card_type": {
                    "credit": [
                        {
                        	"display_name": "Other Cards Credit Qualified",
                            "basis_points": 255,
                            "fixed": 20,
                            "max_interchange": 175
                        },
                        {
                        	"display_name": "Other Cards Credit Mid-Qualified",
                            "basis_points": 325,
                            "fixed": 30,
                            "max_interchange": 239
                        },
                        {
                        	"display_name": "Other Cards Credit Non-Qualified",
                            "basis_points": 375,
                            "fixed": 40
                        }
                    ],
                    "debit": [
                        {
                        	"display_name": "Other Cards Debit Qualified",
                            "basis_points": 225,
                            "fixed": 25,
                            "max_interchange": 160
                        },
                        {
                        	"display_name": "Other Cards Debit Mid-Qualified",
                            "basis_points": 275,
                            "fixed": 35,
                            "max_interchange": 200
                        },
                        {
                        	"display_name": "Other Cards Credit Non-Qualified",
                            "basis_points": 325,
                            "fixed": 40
                        }
                    ]
                }
            },
            "tags": {
                "app_pricing": "qualified billing"
            }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/fee_profiles'
        return formatted_response(endpoint, values, self.platform_encoded_auth, "POST")

    def fetch_application_profile(self, application_profile_id):
        values = None
        endpoint = self.staging_base_url + '/applications/' + application_profile_id + '/application_profile'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def update_application_profile(self, application_profile_id, fee_profile_id):
        values = {
            'fee_profile': fee_profile_id
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/application_profiles/' + application_profile_id
        return formatted_response(endpoint, values, self.platform_encoded_auth, 'PUT')

    def fetch_merchant_profile(self, merchant_profile_id):
        values = None
        endpoint = self.staging_base_url + '/merchant_profiles/' + merchant_profile_id
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def update_merchant_profile(self, merchant_profile_id, fee_profile_id):
        values = {
            'fee_profile': fee_profile_id
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/merchant_profiles/' + merchant_profile_id
        return formatted_response(endpoint, values, self.platform_encoded_auth, 'PUT')


    def update_risk_profile(self, risk_profile_id):
        values = {
            'avs_failure_allowed': False,
            'csc_failure_allowed': False
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/risk_profiles/' + risk_profile_id
        return formatted_response(endpoint, values, self.platform_encoded_auth, 'PUT')

    def remove_transfer(self, settlement_id, transfer_ids):
        values = {
        "transfers": [transfer_ids]
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/settlements/' + settlement_id + '/transfers'
        return formatted_response(endpoint, values, self.platform_encoded_auth, "DELETE")


    def verify_payment_instrument(self, payment_instrument_id, product_type=None):
        values = {
        "processor": "VISA_V1"
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/payment_instruments/' + payment_instrument_id +'/verifications'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)

    def check_card_updater(self, merchant_id, payment_instrument_id):
        values = {
            "merchant": merchant_id
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/payment_instruments/' + payment_instrument_id + '/updates'
        return formatted_response(endpoint, values, self.encoded_auth, "POST")


    def disable_user(self, user_id, toggle_boolean, product_type=None):
        values = {
            "enabled": toggle_boolean
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/users/' + user_id
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.platform_encoded_auth_payouts, 'PUT')
        else:
            return formatted_response(endpoint, values, self.platform_encoded_auth, 'PUT')


    def fund_settlement(self, settlement_id, bank_account_id):
        values = {
            "destination": bank_account_id
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/settlements/' + settlement_id
        return formatted_response(endpoint, values, self.platform_encoded_auth, "PUT")

    def fetch_settlement_split_payout_settlement(self, settlement_id):
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/settlement/settlements/' + settlement_id + "/funding_instruction_preview"
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_settlement_via_review_queue(self):
        values = None
        endpoint = self.staging_base_url + '/review_queue?entity_type=SETTLEMENT&outcome=PENDING'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def approve_settlement_via_review_queue(self, review_queue_id, outcome):
        values = {
            "outcome" : outcome
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/review_queue/' + review_queue_id
        return formatted_response(endpoint, values, self.platform_encoded_auth, 'PUT')


    def review_queue_filter(self, settlement_id):
        values = None
        endpoint = self.staging_base_url + '/review_queue?entity_type=SETTLEMENT&entity_id=' + settlement_id
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_settlement_by_id(self, entity_id):
        values = None
        endpoint = self.staging_base_url + '/settlement_engine/settlements/'+ entity_id
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    # def fetch_funding_instructions_by_settlement(self, entity_id):
    #     values = None
    #     endpoint = self.staging_base_url + '/settlement_engine/settlements/'+ entity_id + '/funding_instructions'
    #     return formatted_response(endpoint, values, self.platform_encoded_auth)

    # def fetch_settlement_fees(self, entity_id):
    #     values = None
    #     endpoint = self.staging_base_url + '/settlement_engine/settlements/'+ entity_id + '/fees'
    #     return formatted_response(endpoint, values, self.platform_encoded_auth)

    def list_fees(self):
        values = None
        endpoint = self.staging_base_url + '/fees'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_fees_by_id(self, fee_id):
        values = None
        endpoint = self.staging_base_url + '/fees/' + fee_id
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def enable_sale(self, application_id):
        values = {
            "application_config" : {
            "card_sale_submission_method" : "real_time"
            }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/applications/' + application_id + "/processors/DUMMY_V1"
        return formatted_response(endpoint, values, self.platform_encoded_auth, 'PUT')

    def create_sale(self, merchant_id, buyer_payment_instrument, amount):
        values = {
         "merchant": merchant_id,
         "currency": "USD",
         "amount": amount,
         "source": buyer_payment_instrument,
         "tags": {
            "test": "sale"
         }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/transfers'
        return formatted_response(endpoint, values, self.encoded_auth)

    def fund_split_payout_settlement(self, settlement_id, bank_account_id):
        values = {
                        "type": "EXPLICIT_AMOUNTS",
                "data": [
                    {
                        "name": "MERCHANT_FUNDING_INSTRUCTION_SPLIT_1",
                        "level": "MERCHANT",
                        "amount": 8255,
                        "currency": "USD",
                        "source_instrument_id": "PI2si4bXXRq8R6AZNxuPVpsH",
                        "destination_instrument_id": bank_account_id,
                        "rail": "PAYFAC_CREDIT"
                    },
                    {
                        "name": "MERCHANT_FUNDING_INSTRUCTION_SPLIT_2",
                        "level": "MERCHANT",
                        "amount": 1000,
                        "currency": "USD",
                        "source_instrument_id": "PI2si4bXXRq8R6AZNxuPVpsH",
                        "destination_instrument_id": "PIu8psXPheWZxCARBrxay2MT",
                        "rail": "PAYFAC_CREDIT"
                    },
                    {
                        "name": "PLATFORM_FUNDING_INSTRUCTION",
                        "level": "PLATFORM",
                        "amount": 745,
                        "currency": "USD",
                        "source_instrument_id": "PI2si4bXXRq8R6AZNxuPVpsH",
                        "destination_instrument_id": "PI7DhFb16hsvseJWz9saB4nL",
                        "rail": "PAYFAC_CREDIT"
                    }
                ]
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/settlements/' + settlement_id
        return formatted_response(endpoint, values, self.platform_encoded_auth, "PUT")

    def toggle_merchant_processing(self, id, toggle_boolean, product_type=None):
        values = {
            "processing_enabled": toggle_boolean
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/merchants/' + id
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.platform_encoded_auth_payouts, 'PUT')
        else:
            return formatted_response(endpoint, values, self.platform_encoded_auth, 'PUT')

    def update_merchant_transfers_settlement_timing(self, id):
        values = {
            "ready_to_settle_upon": "SUCCESSFUL_CAPTURE"
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/merchants/' + id
        return formatted_response(endpoint, values, self.platform_encoded_auth, 'PUT')


    def toggle_merchant_settlements(self, id, toggle_boolean):
        values = {
            "settlement_enabled": toggle_boolean
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/merchants/' + id
        return formatted_response(endpoint, values, self.platform_encoded_auth, "PUT")

    def toggle_application_processing(self, id, toggle_boolean, product_type=None):
        values = {
            "processing_enabled": toggle_boolean
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/applications/' + id
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.platform_encoded_auth_payouts, 'PUT')
        else:
            return formatted_response(endpoint, values, self.platform_encoded_auth, 'PUT')

    def toggle_application_settlements(self, id, toggle_boolean):
        values = {
            "settlement_enabled": toggle_boolean
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/applications/' + id
        return formatted_response(endpoint, values, self.platform_encoded_auth, "PUT")



    def associate_token(self, identity_id, token, product_type=None):
        values = {
            "identity": identity_id,
            "type": "TOKEN",
            "token": token,
            }
        values = format_json(json.dumps(values))

        endpoint = self.staging_base_url + '/payment_instruments'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)



    def create_token(self, application_id, product_type=None):
        values = {
            "expiration_year": 2029,
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
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)


    def create_bank_account(self, identity_id):

        values = {
            "account_type": "SAVINGS",
            "name": "Alice",
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
            "processor": "DUMMY_V1",
            "tags": {
                "order_number": "21DFASJSAKAS"
            },
        }

        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/transfers'
        return formatted_response(endpoint, values, self.encoded_auth)

    def create_debit_idempotency(self, merchant_id, card_id, amount):
        fee = int(round(amount * .1))
        values =  {
            "idempotency_id": uuid.uuid4().hex,
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

    # import ipdb; ipdb.set_trace()
    def create_push_to_card_transfer(self, card_id, amount, currency, type, product_type=None):
        fee = int(round(amount * .1))
        if(type == 'aft'):
            values =  {
                "currency": currency,
                "source": card_id,
                "amount": amount,
                "operation_key": "PULL_FROM_CARD",
                "tags": {
                    "order_number": "21DFASJSAKAS"
                    },
            }
        else:
            values =  {
                "currency": currency,
                "destination": card_id,
                "amount": amount,
                "tags": {
                    "order_number": "21DFASJSAKAS"
                    },
            }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/transfers'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)

    # def create_push_to_card_transfer_aft(self, card_id, amount, currency, product_type=None):
    #     fee = int(round(amount * .1))
    #     values =  {
    #         "currency": currency,
    #         "source": card_id,
    #         "amount": amount,
    #         "operation_key" : "A2",
    #         "tags": {
    #             "order_number": "21DFASJSAKAS"
    #             },
    #     }
    #
    #     values = format_json(json.dumps(values))
    #     endpoint = self.staging_base_url + '/transfers'
    #     if(product_type == 'payouts'):
    #         return formatted_response(endpoint, values, self.encoded_auth_payouts)
    #     else:
    #         return formatted_response(endpoint, values, self.encoded_auth)

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


    def create_refund(self, transfer_id, product_type=None):
        values = """
                  {
                  "refund_amount" : 100
                  }
                """
        endpoint = self.staging_base_url + '/transfers/' + transfer_id + '/reversals'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)

    def reattempt_provision_merchant(self, id):
        values = """
          {}
        """
        endpoint = self.staging_base_url + '/merchants/' + id + '/verifications'
        return formatted_response(endpoint, values, self.encoded_auth)


    def create_webhook(self, product_type=None):
        values = """
                    {
                    "url" : "http://requestb.in/1jb5zu11"
                    }
                """
        endpoint = self.staging_base_url + '/webhooks'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)



    def update_webhook(self, webhook_id, product_type=None):
        values = """
                    {
                    "url" : "https://requestb.in/1bexhoq1"
                    }
        """
        endpoint = self.staging_base_url + '/webhooks/' + webhook_id
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts, 'PUT')
        else:
            return formatted_response(endpoint, values, self.encoded_auth, 'PUT')


    # def create_settlement(self, identity_id, transfer_id):
    #     # transfer_id is the ID of a recently created debit transfer. Here we're
    #     # checking  to see if its ready to settle, typically waiting period
    #     # should be 3600 milliseconds before
    #     # field changes
    #     print ('hit settlement creation')
    #     start = time.time()
    #     minutes = 5
    #     endpoint = self.staging_base_url + '/transfers/' + transfer_id
    #     while not transfer_ready_to_settle(endpoint, self.encoded_auth):
    #         elapsed_time = time.time() - start
    #         if (elapsed_time // 60) % minutes == 0 and elapsed_time > 60:
    #             transfer_response = self.fetch_transfer(transfer_id)
    #             minutes = minutes + 20
    #             counter = stringified_elapsed_time(start)
    #             channel = 'dev'
    #             # This is the full response body
    #             # message = '*Transfer Reconciliation Latency Alert*\nElapsed Time: ' + counter + '\nEnvironment: ' + self.staging_base_url + '\n```' + transfer_response['response_body'] + '```'
    #             # message = '*Transfer Reconciliation Latency Alert* (Exp 3mins)\nElapsed Time: ' + counter + '\nEnvironment: ' + self.staging_base_url + '\nTransfer ID: `' + transfer_response['response_id'] + '`'
    #             # message_slack(channel, message)
    #     values = {
    #         "currency": "USD",
    #         "processor": "DUMMY_V1",
    #         "tags": {
    #             "Internal Daily Settlement ID": "21DFASJSAKAS"
    #         }
    #     }
    #     values = format_json(json.dumps(values))
    #     endpoint = self.staging_base_url + '/identities/' + identity_id + "/settlements"
    #     return formatted_response(endpoint, values, self.encoded_auth)


    def create_split_payout_settlement(self, settlement_id, payment_instrument_id, merchant_identity):
        # transfer_id is the ID of a recently created debit transfer. Here we're
        # checking  to see if its ready to settle, typically waiting period
        # should be 3600 milliseconds before
        # field changes
        # start = time.time()
        # minutes = 5
        # endpoint = self.staging_base_url + '/transfers/' + transfer_id
        # while not transfer_ready_to_settle(endpoint, self.encoded_auth):
        #     elapsed_time = time.time() - start
        #     if (elapsed_time // 60) % minutes == 0 and elapsed_time > 60:
        #         transfer_response = self.fetch_transfer(transfer_id)
        #         minutes = minutes + 20
        #         counter = stringified_elapsed_time(start)
        #         channel = 'dev'
                # This is the full response body
                # message = '*Transfer Reconciliation Latency Alert*\nElapsed Time: ' + counter + '\nEnvironment: ' + self.staging_base_url + '\n```' + transfer_response['response_body'] + '```'
                # message = '*Transfer Reconciliation Latency Alert* (Exp 3mins)\nElapsed Time: ' + counter + '\nEnvironment: ' + self.staging_base_url + '\nTransfer ID: `' + transfer_response['response_id'] + '`'
                # message_slack(channel, message)
        values =  {
             "destination": payment_instrument_id,
             "merchant_identity": merchant_identity,
             "currency": "USD",
             "amount": 200,
             "tags": {
                 "Split Payout ID": "21DFASJSAKAS"
             }
            }

        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/settlements/' + settlement_id + "/funding_transfers"
        return formatted_response(endpoint, values, self.platform_encoded_auth)



    # def fetch_settlement(self, settlement_id):
    #
    #     values = None
    #     endpoint = self.staging_base_url + '/settlements/' + settlement_id
    #     return formatted_response(endpoint, values, self.encoded_auth)


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
        # import ipdb; ipdb.set_trace()

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


        # create dispute by debiting card with amount 888888
        debit = create_debit(self, merchant_id, card_id, 888888)

        # sleeping so that the dispute can be created
        time.sleep(2400)
        # fetch list of all disputes
        headers = {
            'Content-Type': 'application/vnd.json+api',
            'Authorization': 'Basic ' + self.encoded_auth
        }
        # hit disputes index until transfers have a dispute link
        endpoint = self.staging_base_url + '/disputes/'
        request = Request(endpoint, data = None,headers=headers)
        response_body = urlopen(request).read()
        response_body = format_json(response_body)

        values = None
        return formatted_response(endpoint, values, self.encoded_auth)

    def create_authorization(self, merchant_id, card_id):

        values = {
            "currency": "USD",
            "source": card_id,
            "merchant_identity": merchant_id,
            "processor": "DUMMY_V1",
            "amount": 100,
            "tags": {
                "order_number": "21DFASJSAKAS"
            }
            }
        values = format_json(json.dumps(values))

        endpoint = self.staging_base_url + '/authorizations'
        return formatted_response(endpoint, values, self.encoded_auth)

    def create_authorization_idempotency(self, merchant_id, card_id):
        values = {
            "idempotency_id": uuid.uuid4().hex,
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

    def create_subscription_schedule(self):
        values = {
        "name": "test_subscription_schedule",
        "subscription_type": "PERIODIC",
        "period_type": "MONTHLY",
        "period_offset": {
            "month": None,
            "day": 5
           }
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/subscription/subscription_schedules'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_subscription(self, subscription_schedule_id):
        values = None
        endpoint = self.staging_base_url + '/subscription/subscription_schedules/' + subscription_schedule_id
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_subscription_filters(self):
        values = None
        endpoint = self.staging_base_url + '/subscription/subscription_schedules?name=test_subscription_schedule&subscription_type=PERIODIC'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def create_subscription_plan(self):
        values = {
        	"plan_type":"FEE",
        	"name": "plan_name",
        	"fee_plan_data" : {
        		"display_name": "name_group_for_settling",
        		"amount": 54321,
        		"currency": "USD"
        	}
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/subscription/subscription_plans'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_subscription_plan(self, subscription_plan_id):
        values = None
        endpoint = self.staging_base_url + '/subscription/subscription_plans/'+ subscription_plan_id
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_subscription_plan_filters(self):
        values = None
        endpoint = self.staging_base_url + '/subscription/subscription_plans?name=plan_name&subscription_plan_type=FEE'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def create_subscription_group(self, subscription_schedule_id, subscription_plan_id):
        values = {
          	"name": "name",
            "subscription_schedule_id": subscription_schedule_id,
            "subscription_plan_id": subscription_plan_id,
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/subscription/subscription_groups'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_subscription_group(self, subscription_group_id):
        values = None
        endpoint = self.staging_base_url + '/subscription/subscription_groups/'+ subscription_group_id
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_subscription_group_filter(self, subscription_schedule_id, subscription_plan_id, subscription_group_id):
        values = None
        endpoint = self.staging_base_url + '/subscription/subscription_groups/'+ subscription_group_id
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def update_subsciption_group(self, subscription_schedule_id, subscription_plan_id, subscription_group_id):
        values = {
          	"name": "name",
        	"subscription_schedule_id": subscription_schedule_id,
        	"subscription_plan_id": subscription_plan_id
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/subscription/subscription_groups/'+ subscription_group_id
        return formatted_response(endpoint, values, self.platform_encoded_auth, "PATCH")

    def fetch_subscription_group_history(self, subscription_group_id):
        values = None
        endpoint = self.staging_base_url + '/subscription/subscription_groups/'+ subscription_group_id
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def create_subsciption_item(self, merchant_id, subscription_group_id):
        values = {
            "name": "item_name",
        	"merchant_id": merchant_id,
        	"started_at": "2020-03-29T19:47:27.50Z",
        	"ended_at": "2020-05-30T02:00:00Z"
        }
        values = format_json(json.dumps(values))
        endpoint = self.staging_base_url + '/subscription/subscription_groups/'+ subscription_group_id + '/subscription_items'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_subsciption_item(self, subscription_item):
        values = None
        endpoint = self.staging_base_url + '/subscription/subscription_items/'+ subscription_item
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_subsciption_item_filter(self, subscription_group_id,merchant_id):
        values = None
        endpoint = self.staging_base_url + '/subscription/subscription_items?subscription_group_id=' + subscription_group_id +'&merchant_id=' + merchant_id
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def delete_subsciption_item(self, subscription_item):
        values = None
        endpoint = self.staging_base_url + '/subscription/subscription_items/' + subscription_item
        return formatted_response(endpoint, values, self.platform_encoded_auth, "DELETE")

    def fetch_subsciption_item_task_filter(self, subscription_item_id,merchant_id):
        values = None
        endpoint = self.staging_base_url + '/subscription/subscription_items/'+ subscription_item_id +    '/subscription_item_tasks?state=CANCELLED&merchant_id=' + merchant_id
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def fetch_authorization(self, auth_id):
        values = None
        endpoint = self.staging_base_url + '/authorizations/' + auth_id
        return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_dispute(self, dispute_id):

        values = None

        endpoint = self.staging_base_url + '/disputes/' + dispute_id
        return formatted_response(endpoint, values, self.encoded_auth)

    def fetch_user(self, id, product_type=None):
        values = None
        endpoint = self.staging_base_url + '/users/' + id
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_application(self, id, product_type=None):
        values = None
        endpoint = self.staging_base_url + '/applications/' + id
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_identity(self, id, product_type=None):
        values = None
        endpoint = self.staging_base_url + '/identities/' + id
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)


    # def fetch_user(self, id, product_type=None):
    #     values = None
    #     endpoint = self.staging_base_url + '/users/' + id
    #     if(product_type == 'payouts'):
    #         return formatted_response(endpoint, values, self.encoded_auth_payouts)
    #     else:
    #         return formatted_response(endpoint, values, self.encoded_auth)


    def upload_dispute_file(self, dispute_id):

        opener = poster.streaminghttp.register_openers()
        values = {'file': open("testfile.pdf", "rb"), 'name': 'file'}
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

    def fetch_credit_card(self, instrument_id, product_type=None):

        values = None

        endpoint = self.staging_base_url + '/payment_instruments/' + instrument_id
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_identity_verification(self, verification_id):

        values = None

        endpoint = self.staging_base_url + '/verifications/' + verification_id
        return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_transfer(self, transfer_id, product_type=None):

        values = None

        endpoint = self.staging_base_url + '/transfers/' + transfer_id
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)


    def fetch_webhook(self, webhook_id, product_type=None):

        values = None

        endpoint = self.staging_base_url + '/webhooks/' + webhook_id
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)



    def list_authorizations(self):

        values = None
        endpoint = self.staging_base_url + '/authorizations'
        return formatted_response(endpoint, values, self.encoded_auth)


    def list_disputes(self):

        values = None
        endpoint = self.staging_base_url + '/disputes'
        return formatted_response(endpoint, values, self.encoded_auth)


    def list_identities(self, product_type=None):

        values = None
        endpoint = self.staging_base_url + '/identities'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)



    def list_merchants(self):

        values = None
        endpoint = self.staging_base_url + '/merchants'
        return formatted_response(endpoint, values, self.encoded_auth)

    def list_merchant_verifications_platform_user(self, id):
        values = None
        endpoint = self.staging_base_url + '/merchants/' + id + '/verifications'
        return formatted_response(endpoint, values, self.platform_encoded_auth)

    def list_merchant_verifications(self, id, product_type=None):
        values = None
        endpoint = self.staging_base_url + '/merchants/' + id + '/verifications'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)


    def list_payment_instruments(self, product_type=None):
        values = None
        endpoint = self.staging_base_url + '/payment_instruments'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)


    def list_identity_verifications(self):
        values = None
        endpoint = self.staging_base_url + '/verifications'
        return formatted_response(endpoint, values, self.encoded_auth)


    def list_transfers(self, product_type=None):
        values = None
        endpoint = self.staging_base_url + '/transfers'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)


    def list_settlements(self):
        values = None
        endpoint = self.staging_base_url + '/settlements'
        return formatted_response(endpoint, values, self.encoded_auth)


    def list_settlement_transfers(self, id):
        values = None
        endpoint = self.staging_base_url + '/settlements/' + id + '/transfers'
        return formatted_response(endpoint, values, self.encoded_auth)

    # def list_settlement_funding_transfers(self, id):
    #     values = None
    #     endpoint = self.staging_base_url + '/settlements/' + id + '/funding_transfers'
    #     return formatted_response(endpoint, values, self.encoded_auth)

    def list_applications(self, product_type=None):
        values = None
        endpoint = self.staging_base_url + '/applications/'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)

    def list_users(self, product_type=None):
        values = None
        endpoint = self.staging_base_url + '/users/'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)

    def list_webhooks(self, product_type=None):
        values = None
        endpoint = self.staging_base_url + '/webhooks'
        if(product_type == 'payouts'):
            return formatted_response(endpoint, values, self.encoded_auth_payouts)
        else:
            return formatted_response(endpoint, values, self.encoded_auth)
