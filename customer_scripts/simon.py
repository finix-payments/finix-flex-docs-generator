import re
import string
from client import *
from configs import simon
from helpers import format_included_client_header

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

# toggle to skip the settlements bc they always be breaking
TOGGLE_OFF_SETTLEMENTS = True

def create_branded_markdown_docs(template_vars, template_source_file):
    # open up template
    template = open(template_source_file, 'r')
    data = template.read()
    t = MyTemplate(data)
    interpolated_file = t.substitute(template_vars)


    if template_source_file == 'full_docs_template.md':
        # create template for all branded versions of the docs
        file_name = os.getcwd() + "/branded_markdown_docs/" + template_vars["api_name"] + ".html.md"
    else:
        #create admin template
        file_name = os.getcwd() + "/branded_markdown_docs/" + template_vars["api_name"] + "_admin.html.md"

    print 'WRITING to: ' + file_name
    partner_doc_file = open(file_name, 'w')
    partner_doc_file.write(interpolated_file)


def make_all_doc_scenarios(resource_ordering, scenario_ordering, included_clients, destination_file):
    outfile = os.getcwd() + destination_file
    f = open(outfile, 'r+')
    f.truncate()

    if TOGGLE_OFF_SETTLEMENTS == True:
        resource_ordering.remove("settlements")
        scenario_ordering['guide_getting_started'].remove('create_batch_settlement')

    file_ordering = [] # all the file will be inserted into this array according to their ordering
    snippet_directory_location = os.getcwd()

    file = snippet_directory_location + "/sections/slate_configs.md"
    file_ordering.append(file)
    for resource in resource_ordering:
        # iterate over the snippets in the resource directory
        for snippet in scenario_ordering[resource]:

            if snippet == "definition":
                file = snippet_directory_location + "/sections/" + resource + "/" + snippet + ".md"
                file_ordering.append(file)
            else:
                # add the definition for the specific snippet
                file = snippet_directory_location  + "/sections/" + resource + "/" + snippet + "/definition.md"
                file_ordering.append(file)

                # include all the requests for the specific libraries
                for client in included_clients:
                    client = client.lower()
                    file = snippet_directory_location  + "/sections/client_header/" + client + ".md"
                    file_ordering.append(file)
                    file = snippet_directory_location  + "/sections/" + resource + "/" + snippet + "/" + client + "_request.md"
                    file_ordering.append(file)
                    file = snippet_directory_location  + "/sections/client_header/close_parens.md"
                    file_ordering.append(file)
                # add the response for the snippet
                file = snippet_directory_location  + "/sections/" + resource + "/" + snippet + "/response.md"
                file_ordering.append(file)
                # this is an array of snippet directories that dont have specific client requests

    skip_client_scenarios = [
        snippet_directory_location  + "/sections/webhooks/sample_payloads/curl_request.md",
        snippet_directory_location  + "/sections/webhooks/sample_payloads/java_request.md",
        snippet_directory_location  + "/sections/webhooks/sample_payloads/php_request.md",
        snippet_directory_location  + "/sections/webhooks/sample_payloads/python_request.md",
        snippet_directory_location  + "/sections/webhooks/sample_payloads/ruby_request.md"
    ]

    with open(outfile, 'a') as outfile:
        outfile.truncate()
        for fname in file_ordering:
            if fname not in skip_client_scenarios:
                # if fname == "/Users/richardserna2/code/very_good/doc-template-builder/sections/webhooks/sample_payloads/curl_request.md":
                #     import ipdb; ipdb.set_trace()
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
                outfile.write("\n")



def build_docs(config_file):
    # this generates a new version of the template for Non-Admins
    make_all_doc_scenarios(config_file.resource_ordering, config_file.snippets_by_resource, config_file.included_clients, '/full_docs_template.md')

    # this generates a new version of the template for Admins
    make_all_doc_scenarios(config_file.admin_resource_ordering, config_file.admin_snippets_by_resource, config_file.included_clients, '/full_admin_docs_template.md')

    # Create a set of docs for each Partner (i.e. finix customer)
    # for api_configs in config_file.partner_configs:
    print "Building Docs for " + config_file.partner_configs["api_name"]
    included_clients = {"included_clients": format_included_client_header(config_file.included_clients)}
    config_file.partner_configs.update(included_clients)
    template_variables = generate_template_variables(config_file.partner_configs)
    create_branded_markdown_docs(template_variables, 'full_docs_template.md')
    create_branded_markdown_docs(template_variables, 'full_admin_docs_template.md')




def generate_template_variables(config_values):


    ## initialize the API Client
    api_client = Client(staging_base_url = config_values["staging_base_url"],
                        admin_basic_auth_username = config_values["admin_basic_auth_username"],
                        admin_basic_auth_password = config_values["admin_basic_auth_password"],
                        platform_basic_auth_username = config_values["platform_basic_auth_username"],
                        platform_basic_auth_password = config_values["platform_basic_auth_password"],
                        basic_auth_username = "",
                        basic_auth_password = "")

    ## create new user and app
    create_owner_user_scenario = api_client.create_user("ROLE_PARTNER")


    create_app_scenario = api_client.create_app(create_owner_user_scenario["response_id"], "LIMITED_LIABILITY_COMPANY")
    # config_values["application"] = create_app_scenario["response_id"]

    associate_dummyV1_payment_processor_scenario = api_client.associate_payment_processor("DUMMY_V1", create_app_scenario["response_id"])
    create_user_partner_role_scenario = api_client.create_user_partner_role(create_app_scenario["response_id"])
    create_user_platform_role_scenario = api_client.create_user('ROLE_PLATFORM')
    api_client.basic_auth_username = create_owner_user_scenario["response_id"]
    config_values["basic_auth_username"] = create_owner_user_scenario["response_id"]
    api_client.basic_auth_password = json.loads(create_owner_user_scenario["response_body"])['password']
    config_values["basic_auth_password"] = json.loads(create_owner_user_scenario["response_body"])['password']
    api_client.encoded_auth = base64.b64encode(api_client.basic_auth_username + ':' + api_client.basic_auth_password)
    toggle_application_processing_scenario = api_client.toggle_application_processing(create_app_scenario["response_id"], True)
    toggle_application_settlements_scenario = api_client.toggle_application_settlements(create_app_scenario["response_id"], True)


    # FIRST RUN SCENARIOS
    create_webhook_scenario = api_client.create_webhook()
    create_identity_individual_sole_proprietorship_scenario = api_client.create_merchant_identity("INDIVIDUAL_SOLE_PROPRIETORSHIP")
    create_identity_corporation_scenario = api_client.create_merchant_identity("CORPORATION")
    create_identity_limited_liability_company_scenario = api_client.create_merchant_identity("LIMITED_LIABILITY_COMPANY")
    create_identity_partnership_scenario = api_client.create_merchant_identity("PARTNERSHIP")
    create_identity_limited_partnership_scenario = api_client.create_merchant_identity("LIMITED_PARTNERSHIP")
    create_identity_general_partnership_scenario = api_client.create_merchant_identity("GENERAL_PARTNERSHIP")
    create_identity_association_estate_trust_scenario = api_client.create_merchant_identity("ASSOCIATION_ESTATE_TRUST")
    create_identity_tax_exempt_organization_scenario = api_client.create_merchant_identity("TAX_EXEMPT_ORGANIZATION")
    create_identity_international_organization_scenario = api_client.create_merchant_identity("INTERNATIONAL_ORGANIZATION")
    create_identity_government_agency_scenario = api_client.create_merchant_identity("GOVERNMENT_AGENCY")

    create_bank_account_scenario = api_client.create_bank_account(create_identity_individual_sole_proprietorship_scenario["response_id"])
    update_payment_instrument_scenario = api_client.update_payment_instrument(create_bank_account_scenario["response_id"])
    provision_merchant_scenario = api_client.provision_merchant(create_identity_individual_sole_proprietorship_scenario["response_id"])
    create_buyer_identity_scenario = api_client.create_buyer_identity()
    create_card_scenario = api_client.create_card(create_buyer_identity_scenario["response_id"])
    create_buyer_bank_account_scenario = api_client.create_bank_account(create_buyer_identity_scenario["response_id"])
    # account_updater_scenario = account_updater(create_card_scenario["response_id"], provision_merchant_scenario["response_id"])
    create_debit_scenario = api_client.create_debit(create_identity_individual_sole_proprietorship_scenario['response_id'], create_card_scenario["response_id"], random.randint(100, 900000))
    create_bank_debit_scenario = api_client.create_debit(create_identity_individual_sole_proprietorship_scenario['response_id'], create_buyer_bank_account_scenario["response_id"], random.randint(100, 900000))

    create_user_merchant_role_scenario = api_client.create_user_merchant_role(create_identity_individual_sole_proprietorship_scenario["response_id"])
    disable_user_scenario = api_client.disable_user(create_user_merchant_role_scenario["response_id"], False)
    enable_user_scenario = api_client.disable_user(create_user_merchant_role_scenario["response_id"], True)
    # print create_user_merchant_role_scenario
    # create_identity_verification_scenario = create_identity_verification(create_identity_individual_sole_proprietorship_scenario["response_id"])
    create_debit_for_refund_scenario = api_client.create_debit(create_identity_individual_sole_proprietorship_scenario['response_id'], create_card_scenario["response_id"], random.randint(100, 900000))
    create_refund_scenario = api_client.create_refund(create_debit_for_refund_scenario['response_id'])
    create_authorization_scenario = api_client.create_authorization(create_identity_individual_sole_proprietorship_scenario['response_id'], create_card_scenario["response_id"])
    capture_authorization_scenario = api_client.capture_authorization(create_authorization_scenario["response_id"])
    fetch_authorization_scenario = api_client.fetch_authorization(create_authorization_scenario["response_id"])
    create_token_scenario = api_client.create_token(create_app_scenario["response_id"])
    associate_token_scenario = api_client.associate_token(create_identity_individual_sole_proprietorship_scenario["response_id"], create_token_scenario["response_id"])

    create_authorization_for_voiding_scenario = api_client.create_authorization(create_identity_individual_sole_proprietorship_scenario['response_id'], create_card_scenario["response_id"])
    void_authorization_scenario = api_client.void_authorization(create_authorization_for_voiding_scenario["response_id"])

    #check card updater
    check_card_updater_scenario = api_client.check_card_updater(provision_merchant_scenario["response_id"], create_card_scenario["response_id"])

    # FETCH
    fetch_user_scenario = api_client.fetch_user(create_owner_user_scenario["response_id"])
    fetch_application_scenario = api_client.fetch_application(create_app_scenario["response_id"])
    fetch_identity_scenario = api_client.fetch_identity(create_identity_individual_sole_proprietorship_scenario["response_id"])
    fetch_merchant_scenario = api_client.fetch_merchant(provision_merchant_scenario["response_id"])
    fetch_bank_account_scenario = api_client.fetch_bank_account(create_bank_account_scenario["response_id"])
    fetch_credit_card_scenario = api_client.fetch_credit_card(create_card_scenario["response_id"])
    # fetch_identity_verification_scenario = fetch_identity_verification(create_identity_verification_scenario["response_id"])
    fetch_transfer_scenario = api_client.fetch_transfer(create_debit_scenario["response_id"])
    fetch_webhook_scenario = api_client.fetch_webhook(create_webhook_scenario["response_id"])

    # # LIST
    list_authorizations_scenario = api_client.list_authorizations()
    list_disputes_scenario = api_client.list_disputes()
    list_identities_scenario = api_client.list_identities()
    list_merchants_scenario = api_client.list_merchants()
    list_merchant_verifications_scenario = api_client.list_merchant_verifications(provision_merchant_scenario["response_id"])
    list_merchant_verifications_platform_user_scenario = api_client.list_merchant_verifications_platform_user(provision_merchant_scenario["response_id"])
    list_payment_instruments_scenario = api_client.list_payment_instruments()
    # list_identity_verifications_scenario = list_identity_verifications()
    list_transfers_scenario = api_client.list_transfers()
    list_webhooks_scenario = api_client.list_webhooks()
    list_applications_scenario = api_client.list_applications()
    list_users_scenario = api_client.list_users()
    # list_queued_identities_scenario = list_queued_identities()
    # list_queued_merchants_scenario = list_queued_merchants()
    # list_queued_settlements_scenario = list_queued_settlements()
    # fetch_queued_item_scenario = fetch_queued_item()
    # update_queued_state_scenario = update_queued_state()
    update_identity_scenario = api_client.update_identity(create_identity_individual_sole_proprietorship_scenario["response_id"])
    reattempt_provision_merchant_scenario = api_client.reattempt_provision_merchant(provision_merchant_scenario["response_id"])

    # create_dispute_scenario = create_dispute(create_identity_individual_sole_proprietorship_scenario['response_id'], create_card_scenario["response_id"])
    # fetch_dispute_scenario = fetch_dispute(create_dispute_scenario["response_id"])
    # upload_dispute_file_scenario = upload_dispute_file(fetch_dispute_scenario["response_id"])
    if TOGGLE_OFF_SETTLEMENTS == False:
        create_settlement_scenario = api_client.create_settlement(create_identity_individual_sole_proprietorship_scenario['response_id'], create_debit_scenario['response_id'])
        fund_settlement_scenario = api_client.fund_settlement(create_settlement_scenario["response_id"], create_bank_account_scenario["response_id"])
        fetch_settlement_scenario = api_client.fetch_settlement(create_settlement_scenario['response_id'])
        fetch_settlement_transfers_scenario = api_client.fetch_settlement_transfers(create_settlement_scenario['response_id'])
        list_settlement_transfers_scenario = api_client.list_settlement_transfers(create_settlement_scenario["response_id"])
        list_settlement_funding_transfers_scenario = api_client.list_settlement_funding_transfers(fund_settlement_scenario["response_id"])
        list_settlements_scenario = api_client.list_settlements()

    toggle_merchant_processing_scenario = api_client.toggle_merchant_processing(provision_merchant_scenario["response_id"], False)
    toggle_merchant_settlements_scenario = api_client.toggle_merchant_settlements(provision_merchant_scenario["response_id"], False)
    toggle_application_processing_scenario = api_client.toggle_application_processing(create_app_scenario["response_id"], False)
    toggle_application_settlements_scenario = api_client.toggle_application_settlements(create_app_scenario["response_id"], False)

    toggle_on_merchant_processing_scenario = api_client.toggle_merchant_processing(provision_merchant_scenario["response_id"], True)
    toggle_on_merchant_settlements_scenario = api_client.toggle_merchant_settlements(provision_merchant_scenario["response_id"], True)
    toggle_on_application_processing_scenario = api_client.toggle_application_processing(create_app_scenario["response_id"], True)
    toggle_on_application_settlements_scenario = api_client.toggle_application_settlements(create_app_scenario["response_id"], True)

    if TOGGLE_OFF_SETTLEMENTS == False:
        # STORE RESULTS IN HASH FOR TEMPLATE
        api_scenario_vars = {
            # IDENTITIES --------------------------------------------

            "create_merchant_identity_scenario_curl_request": create_identity_individual_sole_proprietorship_scenario["curl_request_body"],
            "create_merchant_identity_scenario_php_request": create_identity_individual_sole_proprietorship_scenario["php_request_body"],
            "create_merchant_identity_scenario_ruby_request": create_identity_individual_sole_proprietorship_scenario["ruby_request_body"],
            "create_merchant_identity_scenario_python_request": create_identity_individual_sole_proprietorship_scenario["python_request_body"],
            "create_merchant_identity_scenario_response": create_identity_individual_sole_proprietorship_scenario["response_body"],
            "create_merchant_identity_scenario_id": create_identity_individual_sole_proprietorship_scenario["response_id"],


            "create_buyer_identity_scenario_curl_request": create_buyer_identity_scenario["curl_request_body"],
            "create_buyer_identity_scenario_php_request": create_buyer_identity_scenario["php_request_body"],
            "create_buyer_identity_scenario_ruby_request": create_buyer_identity_scenario["ruby_request_body"],
            "create_buyer_identity_scenario_python_request": create_buyer_identity_scenario["python_request_body"],
            "create_buyer_identity_scenario_response": create_buyer_identity_scenario["response_body"],
            "create_buyer_identity_scenario_id": create_buyer_identity_scenario["response_id"],

            "update_identity_scenario_curl_request": update_identity_scenario["curl_request_body"],
            "update_identity_scenario_php_request": update_identity_scenario["php_request_body"],
            "update_identity_scenario_ruby_request": update_identity_scenario["ruby_request_body"],
            "update_identity_scenario_python_request": update_identity_scenario["python_request_body"],
            "update_identity_scenario_response": update_identity_scenario["response_body"],
            "update_identity_scenario_id": update_identity_scenario["response_id"],

            "fetch_identity_scenario_response": fetch_identity_scenario["response_body"],
            "fetch_identity_scenario_id": fetch_identity_scenario["response_id"],


            "list_identities_scenario_response": list_identities_scenario["response_body"],

            # MERCHANT VERIFICATIONS
            "list_merchant_verifications_scenario_response": list_merchant_verifications_scenario["response_body"],
            "list_merchant_verifications_platform_user_scenario_response": list_merchant_verifications_scenario["response_body"],


            # MERCHANTS --------------------------------------------

            "provision_merchant_scenario_curl_request": provision_merchant_scenario["curl_request_body"],
            "provision_merchant_scenario_php_request": provision_merchant_scenario["php_request_body"],
            "provision_merchant_scenario_ruby_request": provision_merchant_scenario["ruby_request_body"],
            "provision_merchant_scenario_python_request": provision_merchant_scenario["python_request_body"],
            "provision_merchant_scenario_response": provision_merchant_scenario["response_body"],
            "provision_merchant_scenario_id": provision_merchant_scenario["response_id"],

            "fetch_merchant_scenario_response": fetch_merchant_scenario["response_body"],
            "fetch_merchant_scenario_id": fetch_merchant_scenario["response_id"],

            "reattempt_provision_merchant_scenario_curl_request": reattempt_provision_merchant_scenario["curl_request_body"],
            "reattempt_provision_merchant_scenario_php_request": reattempt_provision_merchant_scenario["php_request_body"],
            "reattempt_provision_merchant_scenario_ruby_request": reattempt_provision_merchant_scenario["ruby_request_body"],
            "reattempt_provision_merchant_scenario_python_request": reattempt_provision_merchant_scenario["python_request_body"],
            "reattempt_provision_merchant_scenario_response": reattempt_provision_merchant_scenario["response_body"],
            "reattempt_provision_merchant_scenario_id": reattempt_provision_merchant_scenario["response_id"],

            "toggle_merchant_processing_scenario_curl_request": toggle_merchant_processing_scenario["curl_request_body"],
            "toggle_merchant_processing_scenario_php_request": toggle_merchant_processing_scenario["php_request_body"],
            "toggle_merchant_processing_scenario_ruby_request": toggle_merchant_processing_scenario["ruby_request_body"],
            "toggle_merchant_processing_scenario_python_request": toggle_merchant_processing_scenario["python_request_body"],
            "toggle_merchant_processing_scenario_response": toggle_merchant_processing_scenario["response_body"],
            "toggle_merchant_processing_scenario_id": toggle_merchant_processing_scenario["response_id"],

            "toggle_merchant_settlements_scenario_curl_request": toggle_merchant_settlements_scenario["curl_request_body"],
            "toggle_merchant_settlements_scenario_php_request": toggle_merchant_settlements_scenario["php_request_body"],
            "toggle_merchant_settlements_scenario_ruby_request": toggle_merchant_settlements_scenario["ruby_request_body"],
            "toggle_merchant_settlements_scenario_python_request": toggle_merchant_settlements_scenario["python_request_body"],
            "toggle_merchant_settlements_scenario_response": toggle_merchant_settlements_scenario["response_body"],
            "toggle_merchant_settlements_scenario_id": toggle_merchant_settlements_scenario["response_id"],

            "list_merchants_scenario_response": list_merchants_scenario["response_body"],

            # IDENTITY VERIFICATION --------------------------

            # "create_identity_verification_scenario_curl_request": create_identity_verification_scenario["curl_request_body"],
            # "create_identity_verification_scenario_php_request": create_identity_verification_scenario["php_request_body"],
            # "create_identity_verification_scenario_ruby_request": create_identity_verification_scenario["ruby_request_body"],
            # "create_identity_verification_scenario_python_request": create_identity_verification_scenario["python_request_body"],
            # "create_identity_verification_scenario_response": create_identity_verification_scenario["response_body"],
            # "create_identity_verification_scenario_id": create_identity_verification_scenario["response_id"],
            #
            # "fetch_identity_verification_scenario_response": fetch_identity_verification_scenario["response_body"],
            # "fetch_identity_verification_scenario_id": fetch_identity_verification_scenario["response_id"],


            # "list_identity_verifications_scenario_curl_request": list_identity_verifications_scenario["curl_request_body"],
            # "list_identity_verifications_scenario_php_request": list_identity_verifications_scenario["php_request_body"],
            # "list_identity_verifications_scenario_ruby_request": list_identity_verifications_scenario["ruby_request_body"],
            # "list_identity_verifications_scenario_python_request": list_identity_verifications_scenario["python_request_body"],
            # "list_identity_verifications_scenario_response": list_identity_verifications_scenario["response_body"],

            # PAYMENT INSTRUMENTS (cards) --------------------------

            "create_card_scenario_curl_request": create_card_scenario["curl_request_body"],
            "create_card_scenario_php_request": create_card_scenario["php_request_body"],
            "create_card_scenario_ruby_request": create_card_scenario["ruby_request_body"],
            "create_card_scenario_python_request": create_card_scenario["python_request_body"],
            "create_card_scenario_response": create_card_scenario["response_body"],
            "create_card_scenario_id": create_card_scenario["response_id"],

            "update_payment_instrument_scenario_curl_request": update_payment_instrument_scenario["curl_request_body"],
            "update_payment_instrument_scenario_php_request": update_payment_instrument_scenario["php_request_body"],
            "update_payment_instrument_scenario_ruby_request": update_payment_instrument_scenario["ruby_request_body"],
            "update_payment_instrument_scenario_python_request": update_payment_instrument_scenario["python_request_body"],
            "update_payment_instrument_scenario_response": update_payment_instrument_scenario["response_body"],
            "update_payment_instrument_scenario_id": update_payment_instrument_scenario["response_id"],

            "check_card_updater_scenario_curl_request": check_card_updater_scenario["curl_request_body"],
            "check_card_updater_scenario_php_request": check_card_updater_scenario["php_request_body"],
            "check_card_updater_scenario_ruby_request": check_card_updater_scenario["ruby_request_body"],
            "check_card_updater_scenario_python_request": check_card_updater_scenario["python_request_body"],
            "check_card_updater_scenario_response": check_card_updater_scenario["response_body"],
            "check_card_updater_scenario_id": check_card_updater_scenario["response_id"],

            # "account_updater_scenario_curl_request": account_updater_scenario["curl_request_body"],
            # "account_updater_scenario_php_request": account_updater_scenario["php_request_body"],
            # "account_updater_scenario_ruby_request": account_updater_scenario["ruby_request_body"],
            # "account_updater_scenario_python_request": account_updater_scenario["python_request_body"],
            # "account_updater_scenario_response": account_updater_scenario["response_body"],
            # "account_updater_scenario_id": account_updater_scenario["response_id"],

            "fetch_bank_account_scenario_response": fetch_bank_account_scenario["response_body"],
            "fetch_bank_account_scenario_id": fetch_bank_account_scenario["response_id"],
            "fetch_credit_card_scenario_response": fetch_credit_card_scenario["response_body"],
            "fetch_credit_card_scenario_id": fetch_credit_card_scenario["response_id"],

            "list_payment_instruments_scenario_response": list_payment_instruments_scenario["response_body"],

            # PAYMENT INSTRUMENTS (bank accounts) --------------------------

            "create_bank_account_scenario_curl_request": create_bank_account_scenario["curl_request_body"],
            "create_bank_account_scenario_php_request": create_bank_account_scenario["php_request_body"],
            "create_bank_account_scenario_ruby_request": create_bank_account_scenario["ruby_request_body"],
            "create_bank_account_scenario_python_request": create_bank_account_scenario["python_request_body"],
            "create_bank_account_scenario_response": create_bank_account_scenario["response_body"],
            "create_bank_account_scenario_id": create_bank_account_scenario["response_id"],


            # TRANSFERS (Debits) --------------------------------------------

            "create_debit_scenario_curl_request": create_debit_scenario["curl_request_body"],
            "create_debit_scenario_php_request": create_debit_scenario["php_request_body"],
            "create_debit_scenario_ruby_request": create_debit_scenario["ruby_request_body"],
            "create_debit_scenario_python_request": create_debit_scenario["python_request_body"],
            "create_debit_scenario_response": create_debit_scenario["response_body"],
            "create_debit_scenario_id": create_debit_scenario["response_id"],

            "fetch_transfer_scenario_response": fetch_transfer_scenario["response_body"],
            "fetch_transfer_scenario_id": fetch_transfer_scenario["response_id"],

            "list_transfers_scenario_response": list_transfers_scenario["response_body"],

            # # TRANSFERS (Credits) --------------------------------------------

            # "create_credit_scenario_curl_request": create_credit_scenario["curl_request_body"],
            # "create_credit_scenario_php_request": create_credit_scenario["php_request_body"],
            # "create_credit_scenario_ruby_request": create_credit_scenario["ruby_request_body"],
            # "create_credit_scenario_python_request": create_credit_scenario["python_request_body"],
            # "create_credit_scenario_response": create_credit_scenario["response_body"],
            # "create_credit_scenario_id": create_credit_scenario["response_id"],

            # "create_bank_debit_scenario_curl_request": create_bank_debit_scenario["curl_request_body"],
            # "create_bank_debit_scenario_php_request": create_bank_debit_scenario["php_request_body"],
            # "create_bank_debit_scenario_ruby_request": create_bank_debit_scenario["ruby_request_body"],
            # "create_bank_debit_scenario_python_request": create_bank_debit_scenario["python_request_body"],
            # "create_bank_debit_scenario_response": create_bank_debit_scenario["response_body"],
            # "create_bank_debit_scenario_id": create_bank_debit_scenario["response_id"],


            #Push-to-card Scenarios
            # "create_recipient_identity_scenario_curl_request": create_recipient_identity_scenario["curl_request_body"],
            # "create_recipient_identity_scenario_php_request": create_recipient_identity_scenario["php_request_body"],
            # "create_recipient_identity_scenario_ruby_request": create_recipient_identity_scenario["ruby_request_body"],
            # "create_recipient_identity_scenario_python_request": create_recipient_identity_scenario["python_request_body"],
            # "create_recipient_identity_scenario_response": create_recipient_identity_scenario["response_body"],
            # "create_recipient_identity_scenario_id": create_recipient_identity_scenario["response_id"],
            #
            # "create_recipient_card_scenario_curl_request": create_recipient_card_scenario["curl_request_body"],
            # "create_recipient_card_scenario_php_request": create_recipient_card_scenario["php_request_body"],
            # "create_recipient_card_scenario_ruby_request": create_recipient_card_scenario["ruby_request_body"],
            # "create_recipient_card_scenario_python_request": create_recipient_card_scenario["python_request_body"],
            # "create_recipient_card_scenario_response": create_recipient_card_scenario["response_body"],
            # "create_recipient_card_scenario_id": create_recipient_card_scenario["response_id"],
            #
            # "provision_merchant_account_scenario_curl_request":  provision_merchant_account_scenario["curl_request_body"],
            # "provision_merchant_account_scenario_response": provision_merchant_account_scenario["response_body"],
            # "provision_merchant_account_scenario_id": provision_merchant_account_scenario["response_id"],
            #
            # "create_recipient_push_to_card_transfer_curl_request": create_recipient_push_to_card_transfer["curl_request_body"],
            # "create_recipient_push_to_card_transfer_php_request": create_recipient_push_to_card_transfer["php_request_body"],
            # "create_recipient_push_to_card_transfer_ruby_request": create_recipient_push_to_card_transfer["ruby_request_body"],
            # "create_recipient_push_to_card_transfer_python_request": create_recipient_push_to_card_transfer["python_request_body"],
            # "create_recipient_push_to_card_transfer_response": create_recipient_push_to_card_transfer["response_body"],
            # "create_recipient_push_to_card_transfer_id": create_recipient_push_to_card_transfer["response_id"],

            # TRANSFERS (Refunds) --------------------------------------------

            "create_refund_scenario_curl_request": create_refund_scenario["curl_request_body"],
            "create_refund_scenario_php_request": create_refund_scenario["php_request_body"],
            "create_refund_scenario_ruby_request": create_refund_scenario["ruby_request_body"],
            "create_refund_scenario_python_request": create_refund_scenario["python_request_body"],
            "create_refund_scenario_response": create_refund_scenario["response_body"],
            "create_refund_scenario_id": create_refund_scenario["response_id"],

            # AUTHORIZATIONS ------------------------------------------------------------

            "create_authorization_scenario_curl_request": create_authorization_scenario["curl_request_body"],
            "create_authorization_scenario_php_request": create_authorization_scenario["php_request_body"],
            "create_authorization_scenario_ruby_request": create_authorization_scenario["ruby_request_body"],
            "create_authorization_scenario_python_request": create_authorization_scenario["python_request_body"],
            "create_authorization_scenario_response": create_authorization_scenario["response_body"],
            "create_authorization_scenario_id": create_authorization_scenario["response_id"],


            "capture_authorization_scenario_curl_request": capture_authorization_scenario["curl_request_body"],
            "capture_authorization_scenario_php_request": capture_authorization_scenario["php_request_body"],
            "capture_authorization_scenario_ruby_request": capture_authorization_scenario["ruby_request_body"],
            "capture_authorization_scenario_python_request": capture_authorization_scenario["python_request_body"],
            "capture_authorization_scenario_response": capture_authorization_scenario["response_body"],
            "capture_authorization_scenario_id": capture_authorization_scenario["response_id"],

            "fetch_authorization_scenario_response": fetch_authorization_scenario["response_body"],
            "fetch_authorization_scenario_id": fetch_authorization_scenario["response_id"],

            "void_authorization_scenario_curl_request": void_authorization_scenario["curl_request_body"],
            "void_authorization_scenario_php_request": void_authorization_scenario["php_request_body"],
            "void_authorization_scenario_ruby_request": void_authorization_scenario["ruby_request_body"],
            "void_authorization_scenario_python_request": void_authorization_scenario["python_request_body"],
            "void_authorization_scenario_response": void_authorization_scenario["response_body"],
            "void_authorization_scenario_id": void_authorization_scenario["response_id"],

            "list_authorizations_scenario_response": list_authorizations_scenario["response_body"],

            # DISPUTES ------------------------------------------------------------
            # "create_dispute_scenario_request": create_dispute_scenario["request_body"],
            # "create_dispute_scenario_response": create_dispute_scenario["response_body"],
            # "create_dispute_scenario_id": create_dispute_scenario["response_id"],
            #
            # "fetch_dispute_scenario_response": fetch_dispute_scenario["response_body"],
            # "fetch_dispute_scenario_id": fetch_dispute_scenario["response_id"],
            #
            #
            # "list_disputes_scenario_response": list_disputes_scenario["response_body"],

            # "upload_dispute_file_scenario_request": upload_dispute_file_scenario["request_body"]    ,
            # "upload_dispute_file_scenario_response": upload_dispute_file_scenario["response_body"],
            # "upload_dispute_file_scenario_id": upload_dispute_file_scenario["response_id"],

            # WEBHOOKS ------------------------------------------------------------

            "create_webhook_scenario_curl_request": create_webhook_scenario["curl_request_body"],
            "create_webhook_scenario_php_request": create_webhook_scenario["php_request_body"],
            "create_webhook_scenario_ruby_request": create_webhook_scenario["ruby_request_body"],
            "create_webhook_scenario_python_request": create_webhook_scenario["python_request_body"],
            "create_webhook_scenario_response": create_webhook_scenario["response_body"],
            "create_webhook_scenario_id": create_webhook_scenario["response_id"],

            "fetch_webhook_scenario_response": fetch_webhook_scenario["response_body"],
            "fetch_webhook_scenario_id": fetch_webhook_scenario["response_id"],

            "list_webhooks_scenario_response": list_webhooks_scenario["response_body"],

            # SETTLEMENTS -----------------------------------------------------
            #


            "create_settlement_scenario_curl_request": create_settlement_scenario["curl_request_body"],
            "create_settlement_scenario_php_request": create_settlement_scenario["php_request_body"],
            "create_settlement_scenario_ruby_request": create_settlement_scenario["ruby_request_body"],
            "create_settlement_scenario_python_request": create_settlement_scenario["python_request_body"],
            "create_settlement_scenario_response": create_settlement_scenario["response_body"],
            "create_settlement_scenario_id": create_settlement_scenario["response_id"],


            "fund_settlement_scenario_curl_request": fund_settlement_scenario["curl_request_body"],
            "fund_settlement_scenario_php_request": fund_settlement_scenario["php_request_body"],
            "fund_settlement_scenario_ruby_request": fund_settlement_scenario["ruby_request_body"],
            "fund_settlement_scenario_python_request": fund_settlement_scenario["python_request_body"],
            "fund_settlement_scenario_response": fund_settlement_scenario["response_body"],
            "fund_settlement_scenario_id": fund_settlement_scenario["response_id"],

            "fetch_settlement_scenario_response": fetch_settlement_scenario["response_body"],
            "fetch_settlement_scenario_id": fetch_settlement_scenario["response_id"],

            "list_settlements_scenario_response": list_settlements_scenario["response_body"],
            "list_settlement_transfers_scenario_response": list_settlement_transfers_scenario["response_body"],
            "list_settlement_funding_transfers_scenario_response": list_settlement_funding_transfers_scenario["response_body"],

            "fetch_settlement_transfers_scenario_request": fetch_settlement_transfers_scenario["request_body"],
            "fetch_settlement_transfers_scenario_response": fetch_settlement_transfers_scenario["response_body"],

            # APPLICATIONS -------------------------------------------------------
            "associate_dummyV1_payment_processor_scenario_curl_request": associate_dummyV1_payment_processor_scenario["curl_request_body"],
            "associate_dummyV1_payment_processor_scenario_php_request": associate_dummyV1_payment_processor_scenario["php_request_body"],
            "associate_dummyV1_payment_processor_scenario_ruby_request": associate_dummyV1_payment_processor_scenario["ruby_request_body"],
            "associate_dummyV1_payment_processor_scenario_python_request": associate_dummyV1_payment_processor_scenario["python_request_body"],
            "associate_dummyV1_payment_processor_scenario_response": associate_dummyV1_payment_processor_scenario["response_body"],
            "associate_dummyV1_payment_processor_scenario_id": associate_dummyV1_payment_processor_scenario["response_id"],

            # "associate_litleV1_payment_processor_scenario_curl_request": associate_litleV1_payment_processor_scenario["curl_request_body"],
            # "associate_litleV1_payment_processor_scenario_php_request": associate_litleV1_payment_processor_scenario["php_request_body"],
            # "associate_litleV1_payment_processor_scenario_ruby_request": associate_litleV1_payment_processor_scenario["ruby_request_body"],
            # "associate_litleV1_payment_processor_scenario_python_request": associate_litleV1_payment_processor_scenario["python_request_body"],
            # "associate_litleV1_payment_processor_scenario_response": associate_litleV1_payment_processor_scenario["response_body"],
            # "associate_litleV1_payment_processor_scenario_id": associate_litleV1_payment_processor_scenario["response_id"],

            "toggle_application_processing_scenario_curl_request": toggle_application_processing_scenario["curl_request_body"],
            "toggle_application_processing_scenario_php_request": toggle_application_processing_scenario["php_request_body"],
            "toggle_application_processing_scenario_ruby_request": toggle_application_processing_scenario["ruby_request_body"],
            "toggle_application_processing_scenario_python_request": toggle_application_processing_scenario["python_request_body"],
            "toggle_application_processing_scenario_response": toggle_application_processing_scenario["response_body"],
            "toggle_application_processing_scenario_id": toggle_application_processing_scenario["response_id"],

            "toggle_application_settlements_scenario_curl_request": toggle_application_settlements_scenario["curl_request_body"],
            "toggle_application_settlements_scenario_php_request": toggle_application_settlements_scenario["php_request_body"],
            "toggle_application_settlements_scenario_ruby_request": toggle_application_settlements_scenario["ruby_request_body"],
            "toggle_application_settlements_scenario_python_request": toggle_application_settlements_scenario["python_request_body"],
            "toggle_application_settlements_scenario_response": toggle_application_settlements_scenario["response_body"],
            "toggle_application_settlements_scenario_id": toggle_application_settlements_scenario["response_id"],

            "toggle_on_application_processing_scenario_curl_request": toggle_on_application_processing_scenario["curl_request_body"],
            "toggle_on_application_processing_scenario_php_request": toggle_on_application_processing_scenario["php_request_body"],
            "toggle_on_application_processing_scenario_ruby_request": toggle_on_application_processing_scenario["ruby_request_body"],
            "toggle_on_application_processing_scenario_python_request": toggle_on_application_processing_scenario["python_request_body"],
            "toggle_on_application_processing_scenario_response": toggle_on_application_processing_scenario["response_body"],
            "toggle_on_application_processing_scenario_id": toggle_on_application_processing_scenario["response_id"],

            "toggle_on_application_settlements_scenario_curl_request": toggle_on_application_settlements_scenario["curl_request_body"],
            "toggle_on_application_settlements_scenario_php_request": toggle_on_application_settlements_scenario["php_request_body"],
            "toggle_on_application_settlements_scenario_ruby_request": toggle_on_application_settlements_scenario["ruby_request_body"],
            "toggle_on_application_settlements_scenario_python_request": toggle_on_application_settlements_scenario["python_request_body"],
            "toggle_on_application_settlements_scenario_response": toggle_on_application_settlements_scenario["response_body"],
            "toggle_on_application_settlements_scenario_id": toggle_on_application_settlements_scenario["response_id"],


            "fetch_application_scenario_response": fetch_application_scenario["response_body"],
            "fetch_application_scenario_id": fetch_application_scenario["response_id"],

            "create_app_scenario_curl_request": create_app_scenario["curl_request_body"],
            "create_app_scenario_php_request": create_app_scenario["php_request_body"],
            "create_app_scenario_ruby_request": create_app_scenario["ruby_request_body"],
            "create_app_scenario_python_request": create_app_scenario["python_request_body"],
            "create_app_scenario_response": create_app_scenario["response_body"],
            "create_app_scenario_id": create_app_scenario["response_id"],

            "list_applications_scenario_response": list_applications_scenario["response_body"],

            # TOKENS -------------------------------------------------------
            "create_token_scenario_request": create_token_scenario["request_body"],
            "create_token_scenario_response": create_token_scenario["response_body"],
            "create_token_scenario_id": create_token_scenario["response_id"],

            "associate_token_scenario_curl_request": associate_token_scenario["curl_request_body"],
            "associate_token_scenario_php_request": associate_token_scenario["php_request_body"],
            "associate_token_scenario_ruby_request": associate_token_scenario["ruby_request_body"],
            "associate_token_scenario_python_request": associate_token_scenario["python_request_body"],
            "associate_token_scenario_response": associate_token_scenario["response_body"],
            "associate_token_scenario_id": associate_token_scenario["response_id"],

            # USERS --------------------------------------------
            "create_owner_user_scenario_curl_request": create_owner_user_scenario["curl_request_body"],
            "create_owner_user_scenario_php_request": create_owner_user_scenario["php_request_body"],
            "create_owner_user_scenario_ruby_request": create_owner_user_scenario["ruby_request_body"],
            "create_owner_user_scenario_python_request": create_owner_user_scenario["python_request_body"],
            "create_owner_user_scenario_response": create_owner_user_scenario["response_body"],
            "create_owner_user_scenario_id": create_owner_user_scenario["response_id"],
            "create_owner_user_scenario_password": json.loads(create_owner_user_scenario["response_body"])['password'],

            "create_user_partner_role_scenario_curl_request": create_user_partner_role_scenario["curl_request_body"],
            "create_user_partner_role_scenario_php_request": create_user_partner_role_scenario["php_request_body"],
            "create_user_partner_role_scenario_ruby_request": create_user_partner_role_scenario["ruby_request_body"],
            "create_user_partner_role_scenario_python_request": create_user_partner_role_scenario["python_request_body"],
            "create_user_partner_role_scenario_response": create_user_partner_role_scenario["response_body"],
            "create_user_partner_role_scenario_id": create_user_partner_role_scenario["response_id"],
            "create_user_partner_role_scenario_password": json.loads(create_user_partner_role_scenario["response_body"])['password'],

            "create_user_merchant_role_scenario_curl_request": create_user_merchant_role_scenario["curl_request_body"],
            "create_user_merchant_role_scenario_php_request": create_user_merchant_role_scenario["php_request_body"],
            "create_user_merchant_role_scenario_ruby_request": create_user_merchant_role_scenario["ruby_request_body"],
            "create_user_merchant_role_scenario_python_request": create_user_merchant_role_scenario["python_request_body"],
            "create_user_merchant_role_scenario_response": create_user_merchant_role_scenario["response_body"],
            "create_user_merchant_role_scenario_id": create_user_merchant_role_scenario["response_id"],
            "create_user_merchant_role_scenario_password": json.loads(create_user_merchant_role_scenario["response_body"])['password'],

            "create_user_platform_role_scenario_curl_request": create_user_platform_role_scenario['curl_request_body'],
            "create_user_platform_role_scenario_php_request": create_user_platform_role_scenario['php_request_body'],
            "create_user_platform_role_scenario_ruby_request": create_user_platform_role_scenario['ruby_request_body'],
            "create_user_platform_role_scenario_python_request": create_user_platform_role_scenario['python_request_body'],
            "create_user_platform_role_scenario_response": create_user_platform_role_scenario["response_body"],
            "create_user_platform_role_scenario_id": create_user_platform_role_scenario["response_id"],
            "create_user_platform_role_scenario_password": json.loads('create_user_platform_role_scenario'["response_body"])['password'],

            "disable_user_scenario_curl_request": disable_user_scenario["curl_request_body"],
            "disable_user_scenario_php_request": disable_user_scenario["php_request_body"],
            "disable_user_scenario_ruby_request": disable_user_scenario["ruby_request_body"],
            "disable_user_scenario_python_request": disable_user_scenario["python_request_body"],
            "disable_user_scenario_response": disable_user_scenario["response_body"],
            "disable_user_scenario_id": disable_user_scenario["response_id"],

            "list_users_scenario_response": list_users_scenario["response_body"],

            "fetch_user_scenario_response": fetch_user_scenario["response_body"],
            "fetch_user_scenario_id": fetch_user_scenario["response_id"],

            # REVIEW QUEUES --------------------------------------------

            # "list_queued_identities_scenario_response": list_queued_identities_scenario["response_body"],
            # "list_queued_merchants_scenario_response": list_queued_merchants_scenario["response_body"],
            # "list_queued_settlements_scenario_response": list_queued_settlements_scenario["response_body"],
            #
            # "fetch_queued_item_scenario_response": fetch_queued_item_scenario["response_body"],
            # "fetch_queued_item_scenario_id": fetch_queued_item_scenario["response_id"],
            #
            # "update_queued_state_scenario_curl_request": update_queued_state_scenario["curl_request_body"],
            # "update_queued_state_scenario_php_request": update_queued_state_scenario["php_request_body"],
            # "update_queued_state_scenario_ruby_request": update_queued_state_scenario["ruby_request_body"],
            # "update_queued_state_scenario_python_request": update_queued_state_scenario["python_request_body"],
            # "update_queued_state_scenario_response": update_queued_state_scenario["response_body"],
            # "update_queued_state_scenario_id": update_queued_state_scenario["response_id"],
            #

        }
    else:
        api_scenario_vars = {
            # IDENTITIES --------------------------------------------

            "create_merchant_identity_scenario_curl_request": create_identity_individual_sole_proprietorship_scenario["curl_request_body"],
            "create_merchant_identity_scenario_php_request": create_identity_individual_sole_proprietorship_scenario["php_request_body"],
            "create_merchant_identity_scenario_ruby_request": create_identity_individual_sole_proprietorship_scenario["ruby_request_body"],
            "create_merchant_identity_scenario_python_request": create_identity_individual_sole_proprietorship_scenario["python_request_body"],
            "create_merchant_identity_scenario_response": create_identity_individual_sole_proprietorship_scenario["response_body"],
            "create_merchant_identity_scenario_id": create_identity_individual_sole_proprietorship_scenario["response_id"],


            "create_buyer_identity_scenario_curl_request": create_buyer_identity_scenario["curl_request_body"],
            "create_buyer_identity_scenario_php_request": create_buyer_identity_scenario["php_request_body"],
            "create_buyer_identity_scenario_ruby_request": create_buyer_identity_scenario["ruby_request_body"],
            "create_buyer_identity_scenario_python_request": create_buyer_identity_scenario["python_request_body"],
            "create_buyer_identity_scenario_response": create_buyer_identity_scenario["response_body"],
            "create_buyer_identity_scenario_id": create_buyer_identity_scenario["response_id"],

            "update_identity_scenario_curl_request": update_identity_scenario["curl_request_body"],
            "update_identity_scenario_php_request": update_identity_scenario["php_request_body"],
            "update_identity_scenario_ruby_request": update_identity_scenario["ruby_request_body"],
            "update_identity_scenario_python_request": update_identity_scenario["python_request_body"],
            "update_identity_scenario_response": update_identity_scenario["response_body"],
            "update_identity_scenario_id": update_identity_scenario["response_id"],

            "fetch_identity_scenario_response": fetch_identity_scenario["response_body"],
            "fetch_identity_scenario_id": fetch_identity_scenario["response_id"],


            "list_identities_scenario_response": list_identities_scenario["response_body"],

            # MERCHANT VERIFICATIONS
            "list_merchant_verifications_scenario_response": list_merchant_verifications_scenario["response_body"],
            "list_merchant_verifications_platform_user_scenario_response": list_merchant_verifications_scenario["response_body"],


            # MERCHANTS --------------------------------------------

            "provision_merchant_scenario_curl_request": provision_merchant_scenario["curl_request_body"],
            "provision_merchant_scenario_php_request": provision_merchant_scenario["php_request_body"],
            "provision_merchant_scenario_ruby_request": provision_merchant_scenario["ruby_request_body"],
            "provision_merchant_scenario_python_request": provision_merchant_scenario["python_request_body"],
            "provision_merchant_scenario_response": provision_merchant_scenario["response_body"],
            "provision_merchant_scenario_id": provision_merchant_scenario["response_id"],

            "fetch_merchant_scenario_response": fetch_merchant_scenario["response_body"],
            "fetch_merchant_scenario_id": fetch_merchant_scenario["response_id"],

            "reattempt_provision_merchant_scenario_curl_request": reattempt_provision_merchant_scenario["curl_request_body"],
            "reattempt_provision_merchant_scenario_php_request": reattempt_provision_merchant_scenario["php_request_body"],
            "reattempt_provision_merchant_scenario_ruby_request": reattempt_provision_merchant_scenario["ruby_request_body"],
            "reattempt_provision_merchant_scenario_python_request": reattempt_provision_merchant_scenario["python_request_body"],
            "reattempt_provision_merchant_scenario_response": reattempt_provision_merchant_scenario["response_body"],
            "reattempt_provision_merchant_scenario_id": reattempt_provision_merchant_scenario["response_id"],

            "toggle_merchant_processing_scenario_curl_request": toggle_merchant_processing_scenario["curl_request_body"],
            "toggle_merchant_processing_scenario_php_request": toggle_merchant_processing_scenario["php_request_body"],
            "toggle_merchant_processing_scenario_ruby_request": toggle_merchant_processing_scenario["ruby_request_body"],
            "toggle_merchant_processing_scenario_python_request": toggle_merchant_processing_scenario["python_request_body"],
            "toggle_merchant_processing_scenario_response": toggle_merchant_processing_scenario["response_body"],
            "toggle_merchant_processing_scenario_id": toggle_merchant_processing_scenario["response_id"],

            "toggle_merchant_settlements_scenario_curl_request": toggle_merchant_settlements_scenario["curl_request_body"],
            "toggle_merchant_settlements_scenario_php_request": toggle_merchant_settlements_scenario["php_request_body"],
            "toggle_merchant_settlements_scenario_ruby_request": toggle_merchant_settlements_scenario["ruby_request_body"],
            "toggle_merchant_settlements_scenario_python_request": toggle_merchant_settlements_scenario["python_request_body"],
            "toggle_merchant_settlements_scenario_response": toggle_merchant_settlements_scenario["response_body"],
            "toggle_merchant_settlements_scenario_id": toggle_merchant_settlements_scenario["response_id"],

            "list_merchants_scenario_response": list_merchants_scenario["response_body"],

            # IDENTITY VERIFICATION --------------------------

            # "create_identity_verification_scenario_curl_request": create_identity_verification_scenario["curl_request_body"],
            # "create_identity_verification_scenario_php_request": create_identity_verification_scenario["php_request_body"],
            # "create_identity_verification_scenario_ruby_request": create_identity_verification_scenario["ruby_request_body"],
            # "create_identity_verification_scenario_python_request": create_identity_verification_scenario["python_request_body"],
            # "create_identity_verification_scenario_response": create_identity_verification_scenario["response_body"],
            # "create_identity_verification_scenario_id": create_identity_verification_scenario["response_id"],
            #
            # "fetch_identity_verification_scenario_response": fetch_identity_verification_scenario["response_body"],
            # "fetch_identity_verification_scenario_id": fetch_identity_verification_scenario["response_id"],


            # "list_identity_verifications_scenario_curl_request": list_identity_verifications_scenario["curl_request_body"],
            # "list_identity_verifications_scenario_php_request": list_identity_verifications_scenario["php_request_body"],
            # "list_identity_verifications_scenario_ruby_request": list_identity_verifications_scenario["ruby_request_body"],
            # "list_identity_verifications_scenario_python_request": list_identity_verifications_scenario["python_request_body"],
            # "list_identity_verifications_scenario_response": list_identity_verifications_scenario["response_body"],

            # PAYMENT INSTRUMENTS (cards) --------------------------

            "create_card_scenario_curl_request": create_card_scenario["curl_request_body"],
            "create_card_scenario_php_request": create_card_scenario["php_request_body"],
            "create_card_scenario_ruby_request": create_card_scenario["ruby_request_body"],
            "create_card_scenario_python_request": create_card_scenario["python_request_body"],
            "create_card_scenario_response": create_card_scenario["response_body"],
            "create_card_scenario_id": create_card_scenario["response_id"],

            "update_payment_instrument_scenario_curl_request": update_payment_instrument_scenario["curl_request_body"],
            "update_payment_instrument_scenario_php_request": update_payment_instrument_scenario["php_request_body"],
            "update_payment_instrument_scenario_ruby_request": update_payment_instrument_scenario["ruby_request_body"],
            "update_payment_instrument_scenario_python_request": update_payment_instrument_scenario["python_request_body"],
            "update_payment_instrument_scenario_response": update_payment_instrument_scenario["response_body"],
            "update_payment_instrument_scenario_id": update_payment_instrument_scenario["response_id"],

            "check_card_updater_scenario_curl_request": check_card_updater_scenario["curl_request_body"],
            "check_card_updater_scenario_php_request": check_card_updater_scenario["php_request_body"],
            "check_card_updater_scenario_ruby_request": check_card_updater_scenario["ruby_request_body"],
            "check_card_updater_scenario_python_request": check_card_updater_scenario["python_request_body"],
            "check_card_updater_scenario_response": check_card_updater_scenario["response_body"],
            "check_card_updater_scenario_id": check_card_updater_scenario["response_id"],

            # "account_updater_scenario_curl_request": account_updater_scenario["curl_request_body"],
            # "account_updater_scenario_php_request": account_updater_scenario["php_request_body"],
            # "account_updater_scenario_ruby_request": account_updater_scenario["ruby_request_body"],
            # "account_updater_scenario_python_request": account_updater_scenario["python_request_body"],
            # "account_updater_scenario_response": account_updater_scenario["response_body"],
            # "account_updater_scenario_id": account_updater_scenario["response_id"],


            "fetch_payment_instrument_scenario_response": fetch_payment_instrument_scenario["response_body"],
            "fetch_payment_instrument_scenario_id": fetch_payment_instrument_scenario["response_id"],

            "list_payment_instruments_scenario_response": list_payment_instruments_scenario["response_body"],

            # PAYMENT INSTRUMENTS (bank accounts) --------------------------

            "create_bank_account_scenario_curl_request": create_bank_account_scenario["curl_request_body"],
            "create_bank_account_scenario_php_request": create_bank_account_scenario["php_request_body"],
            "create_bank_account_scenario_ruby_request": create_bank_account_scenario["ruby_request_body"],
            "create_bank_account_scenario_python_request": create_bank_account_scenario["python_request_body"],
            "create_bank_account_scenario_response": create_bank_account_scenario["response_body"],
            "create_bank_account_scenario_id": create_bank_account_scenario["response_id"],


            # TRANSFERS (Debits) --------------------------------------------

            "create_debit_scenario_curl_request": create_debit_scenario["curl_request_body"],
            "create_debit_scenario_php_request": create_debit_scenario["php_request_body"],
            "create_debit_scenario_ruby_request": create_debit_scenario["ruby_request_body"],
            "create_debit_scenario_python_request": create_debit_scenario["python_request_body"],
            "create_debit_scenario_response": create_debit_scenario["response_body"],
            "create_debit_scenario_id": create_debit_scenario["response_id"],

            "fetch_bank_account_scenario_response": fetch_bank_account_scenario["response_body"],
            "fetch_bank_account_scenario_id": fetch_bank_account_scenario["response_id"],
            "fetch_credit_card_scenario_response": fetch_credit_card_scenario["response_body"],
            "fetch_credit_card_scenario_id": fetch_credit_card_scenario["response_id"],

            "list_transfers_scenario_response": list_transfers_scenario["response_body"],

            # # TRANSFERS (Credits) --------------------------------------------

            # "create_credit_scenario_curl_request": create_credit_scenario["curl_request_body"],
            # "create_credit_scenario_php_request": create_credit_scenario["php_request_body"],
            # "create_credit_scenario_ruby_request": create_credit_scenario["ruby_request_body"],
            # "create_credit_scenario_python_request": create_credit_scenario["python_request_body"],
            # "create_credit_scenario_response": create_credit_scenario["response_body"],
            # "create_credit_scenario_id": create_credit_scenario["response_id"],

            # "create_bank_debit_scenario_curl_request": create_bank_debit_scenario["curl_request_body"],
            # "create_bank_debit_scenario_php_request": create_bank_debit_scenario["php_request_body"],
            # "create_bank_debit_scenario_ruby_request": create_bank_debit_scenario["ruby_request_body"],
            # "create_bank_debit_scenario_python_request": create_bank_debit_scenario["python_request_body"],
            # "create_bank_debit_scenario_response": create_bank_debit_scenario["response_body"],
            # "create_bank_debit_scenario_id": create_bank_debit_scenario["response_id"],


            #Push-to-card Scenarios
            # "create_recipient_identity_scenario_curl_request": create_recipient_identity_scenario["curl_request_body"],
            # "create_recipient_identity_scenario_php_request": create_recipient_identity_scenario["php_request_body"],
            # "create_recipient_identity_scenario_ruby_request": create_recipient_identity_scenario["ruby_request_body"],
            # "create_recipient_identity_scenario_python_request": create_recipient_identity_scenario["python_request_body"],
            # "create_recipient_identity_scenario_response": create_recipient_identity_scenario["response_body"],
            # "create_recipient_identity_scenario_id": create_recipient_identity_scenario["response_id"],
            #
            # "create_recipient_card_scenario_curl_request": create_recipient_card_scenario["curl_request_body"],
            # "create_recipient_card_scenario_php_request": create_recipient_card_scenario["php_request_body"],
            # "create_recipient_card_scenario_ruby_request": create_recipient_card_scenario["ruby_request_body"],
            # "create_recipient_card_scenario_python_request": create_recipient_card_scenario["python_request_body"],
            # "create_recipient_card_scenario_response": create_recipient_card_scenario["response_body"],
            # "create_recipient_card_scenario_id": create_recipient_card_scenario["response_id"],
            #
            # "provision_merchant_account_scenario_curl_request":  provision_merchant_account_scenario["curl_request_body"],
            # "provision_merchant_account_scenario_response": provision_merchant_account_scenario["response_body"],
            # "provision_merchant_account_scenario_id": provision_merchant_account_scenario["response_id"],
            #
            # "create_recipient_push_to_card_transfer_curl_request": create_recipient_push_to_card_transfer["curl_request_body"],
            # "create_recipient_push_to_card_transfer_php_request": create_recipient_push_to_card_transfer["php_request_body"],
            # "create_recipient_push_to_card_transfer_ruby_request": create_recipient_push_to_card_transfer["ruby_request_body"],
            # "create_recipient_push_to_card_transfer_python_request": create_recipient_push_to_card_transfer["python_request_body"],
            # "create_recipient_push_to_card_transfer_response": create_recipient_push_to_card_transfer["response_body"],
            # "create_recipient_push_to_card_transfer_id": create_recipient_push_to_card_transfer["response_id"],

            # TRANSFERS (Refunds) --------------------------------------------

            "create_refund_scenario_curl_request": create_refund_scenario["curl_request_body"],
            "create_refund_scenario_php_request": create_refund_scenario["php_request_body"],
            "create_refund_scenario_ruby_request": create_refund_scenario["ruby_request_body"],
            "create_refund_scenario_python_request": create_refund_scenario["python_request_body"],
            "create_refund_scenario_response": create_refund_scenario["response_body"],
            "create_refund_scenario_id": create_refund_scenario["response_id"],

            # AUTHORIZATIONS ------------------------------------------------------------

            "create_authorization_scenario_curl_request": create_authorization_scenario["curl_request_body"],
            "create_authorization_scenario_php_request": create_authorization_scenario["php_request_body"],
            "create_authorization_scenario_ruby_request": create_authorization_scenario["ruby_request_body"],
            "create_authorization_scenario_python_request": create_authorization_scenario["python_request_body"],
            "create_authorization_scenario_response": create_authorization_scenario["response_body"],
            "create_authorization_scenario_id": create_authorization_scenario["response_id"],


            "capture_authorization_scenario_curl_request": capture_authorization_scenario["curl_request_body"],
            "capture_authorization_scenario_php_request": capture_authorization_scenario["php_request_body"],
            "capture_authorization_scenario_ruby_request": capture_authorization_scenario["ruby_request_body"],
            "capture_authorization_scenario_python_request": capture_authorization_scenario["python_request_body"],
            "capture_authorization_scenario_response": capture_authorization_scenario["response_body"],
            "capture_authorization_scenario_id": capture_authorization_scenario["response_id"],

            "fetch_authorization_scenario_response": fetch_authorization_scenario["response_body"],
            "fetch_authorization_scenario_id": fetch_authorization_scenario["response_id"],

            "void_authorization_scenario_curl_request": void_authorization_scenario["curl_request_body"],
            "void_authorization_scenario_php_request": void_authorization_scenario["php_request_body"],
            "void_authorization_scenario_ruby_request": void_authorization_scenario["ruby_request_body"],
            "void_authorization_scenario_python_request": void_authorization_scenario["python_request_body"],
            "void_authorization_scenario_response": void_authorization_scenario["response_body"],
            "void_authorization_scenario_id": void_authorization_scenario["response_id"],

            "list_authorizations_scenario_response": list_authorizations_scenario["response_body"],

            # DISPUTES ------------------------------------------------------------
            # "create_dispute_scenario_request": create_dispute_scenario["request_body"],
            # "create_dispute_scenario_response": create_dispute_scenario["response_body"],
            # "create_dispute_scenario_id": create_dispute_scenario["response_id"],
            #
            # "fetch_dispute_scenario_response": fetch_dispute_scenario["response_body"],
            # "fetch_dispute_scenario_id": fetch_dispute_scenario["response_id"],
            #
            #
            # "list_disputes_scenario_response": list_disputes_scenario["response_body"],

            # "upload_dispute_file_scenario_request": upload_dispute_file_scenario["request_body"]    ,
            # "upload_dispute_file_scenario_response": upload_dispute_file_scenario["response_body"],
            # "upload_dispute_file_scenario_id": upload_dispute_file_scenario["response_id"],

            # WEBHOOKS ------------------------------------------------------------

            "create_webhook_scenario_curl_request": create_webhook_scenario["curl_request_body"],
            "create_webhook_scenario_php_request": create_webhook_scenario["php_request_body"],
            "create_webhook_scenario_ruby_request": create_webhook_scenario["ruby_request_body"],
            "create_webhook_scenario_python_request": create_webhook_scenario["python_request_body"],
            "create_webhook_scenario_response": create_webhook_scenario["response_body"],
            "create_webhook_scenario_id": create_webhook_scenario["response_id"],

            "fetch_webhook_scenario_response": fetch_webhook_scenario["response_body"],
            "fetch_webhook_scenario_id": fetch_webhook_scenario["response_id"],

            "list_webhooks_scenario_response": list_webhooks_scenario["response_body"],

            # SETTLEMENTS -----------------------------------------------------
            #


            # "create_settlement_scenario_curl_request": create_settlement_scenario["curl_request_body"],
            # "create_settlement_scenario_php_request": create_settlement_scenario["php_request_body"],
            # "create_settlement_scenario_ruby_request": create_settlement_scenario["ruby_request_body"],
            # "create_settlement_scenario_python_request": create_settlement_scenario["python_request_body"],
            # "create_settlement_scenario_response": create_settlement_scenario["response_body"],
            # "create_settlement_scenario_id": create_settlement_scenario["response_id"],
            #
            #
            # "fund_settlement_scenario_curl_request": fund_settlement_scenario["curl_request_body"],
            # "fund_settlement_scenario_php_request": fund_settlement_scenario["php_request_body"],
            # "fund_settlement_scenario_ruby_request": fund_settlement_scenario["ruby_request_body"],
            # "fund_settlement_scenario_python_request": fund_settlement_scenario["python_request_body"],
            # "fund_settlement_scenario_response": fund_settlement_scenario["response_body"],
            # "fund_settlement_scenario_id": fund_settlement_scenario["response_id"],
            #
            # "fetch_settlement_scenario_response": fetch_settlement_scenario["response_body"],
            # "fetch_settlement_scenario_id": fetch_settlement_scenario["response_id"],
            #
            # "list_settlements_scenario_response": list_settlements_scenario["response_body"],
            # "list_settlement_transfers_scenario_response": list_settlement_transfers_scenario["response_body"],
            # "list_settlement_funding_transfers_scenario_response": list_settlement_funding_transfers_scenario["response_body"],
            #
            # "fetch_settlement_transfers_scenario_request": fetch_settlement_transfers_scenario["request_body"],
            # "fetch_settlement_transfers_scenario_response": fetch_settlement_transfers_scenario["response_body"],

            # APPLICATIONS -------------------------------------------------------
            "associate_dummyV1_payment_processor_scenario_curl_request": associate_dummyV1_payment_processor_scenario["curl_request_body"],
            "associate_dummyV1_payment_processor_scenario_php_request": associate_dummyV1_payment_processor_scenario["php_request_body"],
            "associate_dummyV1_payment_processor_scenario_ruby_request": associate_dummyV1_payment_processor_scenario["ruby_request_body"],
            "associate_dummyV1_payment_processor_scenario_python_request": associate_dummyV1_payment_processor_scenario["python_request_body"],
            "associate_dummyV1_payment_processor_scenario_response": associate_dummyV1_payment_processor_scenario["response_body"],
            "associate_dummyV1_payment_processor_scenario_id": associate_dummyV1_payment_processor_scenario["response_id"],

            # "associate_litleV1_payment_processor_scenario_curl_request": associate_litleV1_payment_processor_scenario["curl_request_body"],
            # "associate_litleV1_payment_processor_scenario_php_request": associate_litleV1_payment_processor_scenario["php_request_body"],
            # "associate_litleV1_payment_processor_scenario_ruby_request": associate_litleV1_payment_processor_scenario["ruby_request_body"],
            # "associate_litleV1_payment_processor_scenario_python_request": associate_litleV1_payment_processor_scenario["python_request_body"],
            # "associate_litleV1_payment_processor_scenario_response": associate_litleV1_payment_processor_scenario["response_body"],
            # "associate_litleV1_payment_processor_scenario_id": associate_litleV1_payment_processor_scenario["response_id"],

            "toggle_application_processing_scenario_curl_request": toggle_application_processing_scenario["curl_request_body"],
            "toggle_application_processing_scenario_php_request": toggle_application_processing_scenario["php_request_body"],
            "toggle_application_processing_scenario_ruby_request": toggle_application_processing_scenario["ruby_request_body"],
            "toggle_application_processing_scenario_python_request": toggle_application_processing_scenario["python_request_body"],
            "toggle_application_processing_scenario_response": toggle_application_processing_scenario["response_body"],
            "toggle_application_processing_scenario_id": toggle_application_processing_scenario["response_id"],

            "toggle_application_settlements_scenario_curl_request": toggle_application_settlements_scenario["curl_request_body"],
            "toggle_application_settlements_scenario_php_request": toggle_application_settlements_scenario["php_request_body"],
            "toggle_application_settlements_scenario_ruby_request": toggle_application_settlements_scenario["ruby_request_body"],
            "toggle_application_settlements_scenario_python_request": toggle_application_settlements_scenario["python_request_body"],
            "toggle_application_settlements_scenario_response": toggle_application_settlements_scenario["response_body"],
            "toggle_application_settlements_scenario_id": toggle_application_settlements_scenario["response_id"],

            "toggle_on_application_processing_scenario_curl_request": toggle_on_application_processing_scenario["curl_request_body"],
            "toggle_on_application_processing_scenario_php_request": toggle_on_application_processing_scenario["php_request_body"],
            "toggle_on_application_processing_scenario_ruby_request": toggle_on_application_processing_scenario["ruby_request_body"],
            "toggle_on_application_processing_scenario_python_request": toggle_on_application_processing_scenario["python_request_body"],
            "toggle_on_application_processing_scenario_response": toggle_on_application_processing_scenario["response_body"],
            "toggle_on_application_processing_scenario_id": toggle_on_application_processing_scenario["response_id"],

            "toggle_on_application_settlements_scenario_curl_request": toggle_on_application_settlements_scenario["curl_request_body"],
            "toggle_on_application_settlements_scenario_php_request": toggle_on_application_settlements_scenario["php_request_body"],
            "toggle_on_application_settlements_scenario_ruby_request": toggle_on_application_settlements_scenario["ruby_request_body"],
            "toggle_on_application_settlements_scenario_python_request": toggle_on_application_settlements_scenario["python_request_body"],
            "toggle_on_application_settlements_scenario_response": toggle_on_application_settlements_scenario["response_body"],
            "toggle_on_application_settlements_scenario_id": toggle_on_application_settlements_scenario["response_id"],


            "fetch_application_scenario_response": fetch_application_scenario["response_body"],
            "fetch_application_scenario_id": fetch_application_scenario["response_id"],

            "create_app_scenario_curl_request": create_app_scenario["curl_request_body"],
            "create_app_scenario_php_request": create_app_scenario["php_request_body"],
            "create_app_scenario_ruby_request": create_app_scenario["ruby_request_body"],
            "create_app_scenario_python_request": create_app_scenario["python_request_body"],
            "create_app_scenario_response": create_app_scenario["response_body"],
            "create_app_scenario_id": create_app_scenario["response_id"],

            "list_applications_scenario_response": list_applications_scenario["response_body"],

            # TOKENS -------------------------------------------------------
            "create_token_scenario_request": create_token_scenario["request_body"],
            "create_token_scenario_response": create_token_scenario["response_body"],
            "create_token_scenario_id": create_token_scenario["response_id"],

            "associate_token_scenario_curl_request": associate_token_scenario["curl_request_body"],
            "associate_token_scenario_php_request": associate_token_scenario["php_request_body"],
            "associate_token_scenario_ruby_request": associate_token_scenario["ruby_request_body"],
            "associate_token_scenario_python_request": associate_token_scenario["python_request_body"],
            "associate_token_scenario_response": associate_token_scenario["response_body"],
            "associate_token_scenario_id": associate_token_scenario["response_id"],

            # USERS --------------------------------------------
            "create_owner_user_scenario_curl_request": create_owner_user_scenario["curl_request_body"],
            "create_owner_user_scenario_php_request": create_owner_user_scenario["php_request_body"],
            "create_owner_user_scenario_ruby_request": create_owner_user_scenario["ruby_request_body"],
            "create_owner_user_scenario_python_request": create_owner_user_scenario["python_request_body"],
            "create_owner_user_scenario_response": create_owner_user_scenario["response_body"],
            "create_owner_user_scenario_id": create_owner_user_scenario["response_id"],
            "create_owner_user_scenario_password": json.loads(create_owner_user_scenario["response_body"])['password'],

            "create_user_partner_role_scenario_curl_request": create_user_partner_role_scenario["curl_request_body"],
            "create_user_partner_role_scenario_php_request": create_user_partner_role_scenario["php_request_body"],
            "create_user_partner_role_scenario_ruby_request": create_user_partner_role_scenario["ruby_request_body"],
            "create_user_partner_role_scenario_python_request": create_user_partner_role_scenario["python_request_body"],
            "create_user_partner_role_scenario_response": create_user_partner_role_scenario["response_body"],
            "create_user_partner_role_scenario_id": create_user_partner_role_scenario["response_id"],
            "create_user_partner_role_scenario_password": json.loads(create_user_partner_role_scenario["response_body"])['password'],

            "create_user_merchant_role_scenario_curl_request": create_user_merchant_role_scenario["curl_request_body"],
            "create_user_merchant_role_scenario_php_request": create_user_merchant_role_scenario["php_request_body"],
            "create_user_merchant_role_scenario_ruby_request": create_user_merchant_role_scenario["ruby_request_body"],
            "create_user_merchant_role_scenario_python_request": create_user_merchant_role_scenario["python_request_body"],
            "create_user_merchant_role_scenario_response": create_user_merchant_role_scenario["response_body"],
            "create_user_merchant_role_scenario_id": create_user_merchant_role_scenario["response_id"],
            "create_user_merchant_role_scenario_password": json.loads(create_user_merchant_role_scenario["response_body"])['password'],

            "create_user_platform_role_scenario_curl_request": create_user_platform_role_scenario['curl_request_body'],
            "create_user_platform_role_scenario_php_request": create_user_platform_role_scenario['php_request_body'],
            "create_user_platform_role_scenario_ruby_request": create_user_platform_role_scenario['ruby_request_body'],
            "create_user_platform_role_scenario_python_request": create_user_platform_role_scenario['python_request_body'],
            "create_user_platform_role_scenario_response": create_user_platform_role_scenario["response_body"],
            "create_user_platform_role_scenario_id": create_user_platform_role_scenario["response_id"],
            "create_user_platform_role_scenario_password": json.loads('create_user_platform_role_scenario'["response_body"])['password'],

            "disable_user_scenario_curl_request": disable_user_scenario["curl_request_body"],
            "disable_user_scenario_php_request": disable_user_scenario["php_request_body"],
            "disable_user_scenario_ruby_request": disable_user_scenario["ruby_request_body"],
            "disable_user_scenario_python_request": disable_user_scenario["python_request_body"],
            "disable_user_scenario_response": disable_user_scenario["response_body"],
            "disable_user_scenario_id": disable_user_scenario["response_id"],

            "list_users_scenario_response": list_users_scenario["response_body"],

            "fetch_user_scenario_response": fetch_user_scenario["response_body"],
            "fetch_user_scenario_id": fetch_user_scenario["response_id"],

            # REVIEW QUEUES --------------------------------------------

            # "list_queued_identities_scenario_response": list_queued_identities_scenario["response_body"],
            # "list_queued_merchants_scenario_response": list_queued_merchants_scenario["response_body"],
            # "list_queued_settlements_scenario_response": list_queued_settlements_scenario["response_body"],
            #
            # "fetch_queued_item_scenario_response": fetch_queued_item_scenario["response_body"],
            # "fetch_queued_item_scenario_id": fetch_queued_item_scenario["response_id"],
            #
            # "update_queued_state_scenario_curl_request": update_queued_state_scenario["curl_request_body"],
            # "update_queued_state_scenario_php_request": update_queued_state_scenario["php_request_body"],
            # "update_queued_state_scenario_ruby_request": update_queued_state_scenario["ruby_request_body"],
            # "update_queued_state_scenario_python_request": update_queued_state_scenario["python_request_body"],
            # "update_queued_state_scenario_response": update_queued_state_scenario["response_body"],
            # "update_queued_state_scenario_id": update_queued_state_scenario["response_id"],
            #

        }


    # COMBINE CONFIGS W/ SCENARIO VARs
    template_vars = config_values.copy()
    template_vars.update(api_scenario_vars)
    return template_vars


build_docs(simon)