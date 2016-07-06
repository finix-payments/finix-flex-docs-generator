import re
import string
import random
from seed_client import *
from configs import snippets_by_resource, resource_ordering, included_clients, \
    partner_configs


partner_configs = { 'api_name': "Finix",
        'api_name_downcase': "finix",
        'base_url': 'https://api-staging.finix.io',
        'basic_auth_username': "USssB2ix2pnSabNNTUkmELof",
        'basic_auth_password': "6b7881ed-704a-434f-89f1-0f461d7b91d7",
        'encoded_auth': base64.b64encode('USssB2ix2pnSabNNTUkmELof:6b7881ed-704a-434f-89f1-0f461d7b91d7'),
        'admin_basic_auth_username': 'US7AQLoX6FtZcPDttFAafEz2',
        'admin_basic_auth_password': 'f3276399-20f4-4bc3-aff0-71131cb347b8',
        'admin_encoded_auth': base64.b64encode('US7AQLoX6FtZcPDttFAafEz2:f3276399-20f4-4bc3-aff0-71131cb347b8'),
        'payment_processor': "DUMMY_V1",
        'identity_verification_processor': "DUMMY_V1",
        'application': "APbmgzh7p41hxissnqgEFHJT",
        'jsfiddle': "http://jsfiddle.net/rserna2010/2hxnjL0q/"
    }

def seed_database(config_values):
    ## create new user and app


    buyer_ids = []
    card_ids = []
    # FIRST create all the buyers
    for x in range(0, 23):
            create_buyer_scenario = create_buyer_identity(config_values)
            buyer_id = create_buyer_scenario["response_id"]
            buyer_ids.append(buyer_id)
            create_card_scenario = create_card(config_values, buyer_id)
            card_id = create_card_scenario["response_id"]
            card_ids.append(card_id)

    for x in range(0, 120):
        card = random.choice (card_ids)
        create_debit_scenario = create_debit(config_values, "IDijNjLLr2XdE3wn5GZbbLyF", card, random.randint(100, 1000000))
        print create_debit_scenario["response_body"]

    for x in range(0, 78):
        card = random.choice (card_ids)
        create_debit_scenario = create_debit(config_values, "IDijNjLLr2XdE3wn5GZbbLyF", card, 102)




seed_database(partner_configs)

def create_apps(config_values):
    pay_facs = ["HyperWallet", "Venmo", "Square", "Paypal", "Dwolla", "WePay", "Facebook", "Google", "BrainTree"]

    for x in pay_facs:
        create_user_scenario = create_user(config_values, "ROLE_PARTNER")
        create_app_scenario = create_app(config_values, create_user_scenario["response_id"], x)
        print create_app_scenario
        config_values["application"] = create_app_scenario["response_id"]
        associate_payment_processor_scenario = associate_payment_processor(config_values)
        if config_values["payment_processor"] != "DUMMY_V1":
            associate_identity_verification_processor_scenario = associate_identity_verification_processor(config_values)
        create_user_partner_role_scenario = create_user_partner_role(config_values)
        config_values["basic_auth_username"] = create_user_scenario["response_id"]
        config_values["basic_auth_password"] = json.loads(create_user_scenario["response_body"])['password']
        config_values["encoded_auth"] = base64.b64encode(config_values["basic_auth_username"] + ':' + config_values["basic_auth_password"])

# create_apps(partner_configs)