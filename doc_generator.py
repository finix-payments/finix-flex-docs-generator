import re
import string
from client import *
from configs import snippets_by_resource, resource_ordering, included_clients, \
    partner_configs, admin_snippets_by_resource, admin_resource_ordering
from finix_configs import finix_snippets_by_resource, finix_resource_ordering, finix_included_clients, \
    finix_partner_configs, finix_admin_snippets_by_resource, finix_admin_resource_ordering    

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

def create_client_specific_templates(template_vars):
    snippet_directory_location = os.getcwd()
    for client in included_clients:
        print 'WRITING ' + client + " client-specific request template and script"
        template = open(os.getcwd() + '/client_specific_templates/' + client + '_template.md', 'r')
        data = template.read()
        t = MyTemplate(data)
        interpolated_file = t.substitute(template_vars)

        if client == "php":
            partner_doc_file = open(snippet_directory_location + '/client_specific_templates/php_test.php', 'w')
        elif client == "java":
            partner_doc_file = open(snippet_directory_location + '/client_specific_templates/java_test.java', 'w')
        elif client == "curl":
            partner_doc_file = open(snippet_directory_location + '/client_specific_templates/curl_test.txt', 'w')
        partner_doc_file.write(interpolated_file)

def make_all_doc_scenarios(resource_ordering, scenario_ordering, destination_file):
    outfile = os.getcwd() + destination_file
    f = open(outfile, 'r+')
    f.truncate()

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


# This method just takes all the snippet scenarios for a particular client language
# and creates a file with just that languages specific requests
def make_client_specific_scenarios():

    for client in included_clients:
        # all the file will be inserted into this array according to their ordering
        file_ordering = []
        snippet_directory_location = os.getcwd()

        outfile = os.getcwd() + '/client_specific_templates/' + client + '_template.md'
        f = open(outfile, 'r+')
        f.truncate()

        for resource in resource_ordering:
            # iterate over the snippets in the resource directory
            for snippet in snippets_by_resource[resource]:

                if snippet == "definition":
                    continue
                else:
                    file = snippet_directory_location  + "/sections/" + resource + "/" + snippet + "/" + client + "_request.md"
                    file_ordering.append(file)

        with open(outfile, 'a') as outfile:
            outfile.truncate()

            file = snippet_directory_location  + "/sections/client_header/" + client + ".md"
            with open(file) as infile:
                next(infile)
                for line in infile:
                    outfile.write

            for fname in file_ordering:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
                outfile.write("\n")

def build_docs():

    if not finix_partner_configs: 
        # this generates a new version of the template for Non-Admins
        make_all_doc_scenarios(resource_ordering, snippets_by_resource, '/full_docs_template.md')

        # this generates a new version of the template for Admins
        make_all_doc_scenarios(admin_resource_ordering, admin_snippets_by_resource, '/full_admin_docs_template.md')

        # Create a set of docs for each Partner (i.e. finix customer)
    for api_configs in partner_configs:
        print "Building Docs for " + api_configs["api_name"]
        template_variables = generate_template_variables(api_configs)
        create_branded_markdown_docs(template_variables, 'full_docs_template.md')
        create_branded_markdown_docs(template_variables, 'full_admin_docs_template.md')
    else:    
        # this generates a new version of the template for Non-Admins
        make_all_doc_scenarios(finix_resource_ordering, finix_snippets_by_resource, '/full_docs_template.md')

        # this generates a new version of the template for Admins
        make_all_doc_scenarios(finix_admin_resource_ordering, finix_admin_snippets_by_resource, '/full_admin_docs_template.md')

        # Create a set of docs for each Partner (i.e. finix customer)
    for api_configs in finix_partner_configs:
        print "Building Docs for " + api_configs["api_name"]
        template_variables = generate_template_variables(api_configs)
        create_branded_markdown_docs(template_variables, 'full_docs_template.md')
        create_branded_markdown_docs(template_variables, 'full_admin_docs_template.md')

        # this generates the Client-library specific version of the snippets template which you can use to test the API calls
        # make_client_specific_scenarios()
        # create_client_specific_templates(template_variables)


def generate_template_variables(config_values):
    ## create new user and app
    create_owner_user_scenario = create_user(config_values, "ROLE_PARTNER")

    create_app_scenario = create_app(config_values, create_owner_user_scenario["response_id"], "LIMITED_LIABILITY_COMPANY")
    config_values["application"] = create_app_scenario["response_id"]

    associate_dummyV1_payment_processor_scenario = associate_payment_processor(config_values, "DUMMY_V1")
    # associate_litleV1_payment_processor_scenario = associate_payment_processor(config_values, "LITLE_V1")
    # if config_values["payment_processor"] != "DUMMY_V1":
    #     associate_identity_verification_processor_scenario = associate_identity_verification_processor(config_values)
    create_user_partner_role_scenario = create_user_partner_role(config_values)
    config_values["basic_auth_username"] = create_owner_user_scenario["response_id"]
    config_values["basic_auth_password"] = json.loads(create_owner_user_scenario["response_body"])['password']
    config_values["encoded_auth"] = base64.b64encode(config_values["basic_auth_username"] + ':' + config_values["basic_auth_password"])
    toggle_application_processing_scenario = toggle_application_processing(config_values, create_app_scenario["response_id"], True)
    toggle_application_settlements_scenario = toggle_application_settlements(config_values, create_app_scenario["response_id"], True)


    # FIRST RUN SCENARIOS
    create_webhook_scenario = create_webhook(config_values)
    create_identity_individual_sole_proprietorship_scenario = create_merchant_identity(config_values, "INDIVIDUAL_SOLE_PROPRIETORSHIP")
    create_identity_corporation_scenario = create_merchant_identity(config_values, "CORPORATION")
    create_identity_limited_liability_company_scenario = create_merchant_identity(config_values, "LIMITED_LIABILITY_COMPANY")
    create_identity_partnership_scenario = create_merchant_identity(config_values, "PARTNERSHIP")
    create_identity_limited_partnership_scenario = create_merchant_identity(config_values, "LIMITED_PARTNERSHIP")
    create_identity_general_partnership_scenario = create_merchant_identity(config_values, "GENERAL_PARTNERSHIP")
    create_identity_association_estate_trust_scenario = create_merchant_identity(config_values, "ASSOCIATION_ESTATE_TRUST")
    create_identity_tax_exempt_organization_scenario = create_merchant_identity(config_values, "TAX_EXEMPT_ORGANIZATION")
    create_identity_international_organization_scenario = create_merchant_identity(config_values, "INTERNATIONAL_ORGANIZATION")
    create_identity_government_agency_scenario = create_merchant_identity(config_values, "GOVERNMENT_AGENCY")

    create_bank_account_scenario = create_bank_account(config_values, create_identity_individual_sole_proprietorship_scenario["response_id"])
    update_payment_instrument_scenario = update_payment_instrument(config_values, create_bank_account_scenario["response_id"])
    provision_merchant_scenario = provision_merchant(config_values, create_identity_individual_sole_proprietorship_scenario["response_id"])
    create_buyer_identity_scenario = create_buyer_identity(config_values)
    create_card_scenario = create_card(config_values, create_buyer_identity_scenario["response_id"])
    create_buyer_bank_account_scenario = create_bank_account(config_values, create_buyer_identity_scenario["response_id"])
    # account_updater_scenario = account_updater(config_values, create_card_scenario["response_id"], provision_merchant_scenario["response_id"])
    create_debit_scenario = create_debit(config_values, create_identity_individual_sole_proprietorship_scenario['response_id'], create_card_scenario["response_id"], random.randint(100, 900000))
    create_bank_debit_scenario = create_debit(config_values, create_identity_individual_sole_proprietorship_scenario['response_id'], create_buyer_bank_account_scenario["response_id"], random.randint(100, 900000))

    create_user_merchant_role_scenario = create_user_merchant_role(config_values, create_identity_individual_sole_proprietorship_scenario["response_id"])
    disable_user_scenario = disable_user(config_values, create_user_merchant_role_scenario["response_id"], False)
    enable_user_scenario = disable_user(config_values, create_user_merchant_role_scenario["response_id"], True)
    # print create_user_merchant_role_scenario
    # create_identity_verification_scenario = create_identity_verification(config_values, create_identity_individual_sole_proprietorship_scenario["response_id"])
    create_refund_scenario = create_refund(config_values, create_debit_scenario['response_id'])
    create_authorization_scenario = create_authorization(config_values, create_identity_individual_sole_proprietorship_scenario['response_id'], create_card_scenario["response_id"])
    capture_authorization_scenario = capture_authorization(config_values, create_authorization_scenario["response_id"])
    fetch_authorization_scenario = fetch_authorization(config_values, create_authorization_scenario["response_id"])
    create_token_scenario = create_token(config_values)
    associate_token_scenario = associate_token(config_values, create_identity_individual_sole_proprietorship_scenario["response_id"], create_token_scenario["response_id"])

    create_authorization_for_voiding_scenario = create_authorization(config_values, create_identity_individual_sole_proprietorship_scenario['response_id'], create_card_scenario["response_id"])
    void_authorization_scenario = void_authorization(config_values, create_authorization_for_voiding_scenario["response_id"])

    # FETCH
    fetch_user_scenario = fetch_user(config_values, create_owner_user_scenario["response_id"])
    fetch_application_scenario = fetch_application(config_values, create_app_scenario["response_id"])
    fetch_identity_scenario = fetch_identity(config_values, create_identity_individual_sole_proprietorship_scenario["response_id"])
    fetch_merchant_scenario = fetch_merchant(config_values, provision_merchant_scenario["response_id"])
    fetch_payment_instrument_scenario = fetch_payment_instrument(config_values, create_bank_account_scenario["response_id"])
    # fetch_identity_verification_scenario = fetch_identity_verification(config_values, create_identity_verification_scenario["response_id"])
    fetch_transfer_scenario = fetch_transfer(config_values, create_debit_scenario["response_id"])
    fetch_webhook_scenario = fetch_webhook(config_values, create_webhook_scenario["response_id"])

    #Push-to-card Scenarios
    associate_payment_processor_push_to_card_scenario = associate_payment_processor(config_values, "VISA_V1")    
    create_recipient_identity_scenario = create_buyer_identity(config_values)
    create_recipient_card_scenario = create_card(config_values, create_recipient_identity_scenario["response_id"])
    create_recipient_push_to_card_transfer = create_push_to_card_transfer(config_values, create_recipient_identity_scenario["response_id"], create_recipient_card_scenario["response_id"], 10000)

    # LIST
    list_authorizations_scenario = list_authorizations(config_values)
    list_disputes_scenario = list_disputes(config_values)
    list_identities_scenario = list_identities(config_values)
    list_merchants_scenario = list_merchants(config_values)
    list_merchant_verifications_scenario = list_merchant_verifications(config_values, provision_merchant_scenario["response_id"])
    list_merchant_verifications_platform_user_scenario = list_merchant_verifications_platform_user(config_values, provision_merchant_scenario["response_id"])
    list_payment_instruments_scenario = list_payment_instruments(config_values)
    # list_identity_verifications_scenario = list_identity_verifications(config_values)
    list_transfers_scenario = list_transfers(config_values)
    list_webhooks_scenario = list_webhooks(config_values)
    list_applications_scenario = list_applications(config_values)
    list_users_scenario = list_users(config_values)
    # list_queued_identities_scenario = list_queued_identities(config_values)
    # list_queued_merchants_scenario = list_queued_merchants(config_values)
    # list_queued_settlements_scenario = list_queued_settlements(config_values)
    # fetch_queued_item_scenario = fetch_queued_item(config_values)
    # update_queued_state_scenario = update_queued_state(config_values)
    update_identity_scenario = update_identity(config_values, create_identity_individual_sole_proprietorship_scenario["response_id"])
    reattempt_provision_merchant_scenario = reattempt_provision_merchant(config_values, provision_merchant_scenario["response_id"])

    # create_dispute_scenario = create_dispute(config_values, create_identity_individual_sole_proprietorship_scenario['response_id'], create_card_scenario["response_id"])
    # fetch_dispute_scenario = fetch_dispute(config_values, create_dispute_scenario["response_id"])
    # upload_dispute_file_scenario = upload_dispute_file(config_values, fetch_dispute_scenario["response_id"])
    create_settlement_scenario = create_settlement(config_values, create_identity_individual_sole_proprietorship_scenario['response_id'])
    fund_settlement_scenario = fund_settlement(config_values, create_settlement_scenario["response_id"], create_bank_account_scenario["response_id"])
    fetch_settlement_scenario = fetch_settlement(config_values, create_settlement_scenario['response_id'])
    fetch_settlement_transfers_scenario = fetch_settlement_transfers(config_values, create_settlement_scenario['response_id'])
    list_settlements_scenario = list_settlements(config_values)
    list_settlement_transfers_scenario = list_settlement_transfers(config_values, create_settlement_scenario["response_id"])
    list_settlement_funding_transfers_scenario = list_settlement_funding_transfers(config_values, fund_settlement_scenario["response_id"])
    toggle_merchant_processing_scenario = toggle_merchant_processing(config_values, provision_merchant_scenario["response_id"], False)
    toggle_merchant_settlements_scenario = toggle_merchant_settlements(config_values, provision_merchant_scenario["response_id"], False)
    toggle_application_processing_scenario = toggle_application_processing(config_values, create_app_scenario["response_id"], False)
    toggle_application_settlements_scenario = toggle_application_settlements(config_values, create_app_scenario["response_id"], False)

    toggle_on_merchant_processing_scenario = toggle_merchant_processing(config_values, provision_merchant_scenario["response_id"], True)
    toggle_on_merchant_settlements_scenario = toggle_merchant_settlements(config_values, provision_merchant_scenario["response_id"], True)
    toggle_on_application_processing_scenario = toggle_application_processing(config_values, create_app_scenario["response_id"], True)
    toggle_on_application_settlements_scenario = toggle_application_settlements(config_values, create_app_scenario["response_id"], True)


    # STORE RESULTS IN HASH FOR TEMPLATE
    api_scenario_vars = {
        # IDENTITIES --------------------------------------------

        "create_merchant_identity_scenario_curl_request": create_identity_individual_sole_proprietorship_scenario["curl_request_body"],
        "create_merchant_identity_scenario_php_request": create_identity_individual_sole_proprietorship_scenario["php_request_body"],
        "create_merchant_identity_scenario_response": create_identity_individual_sole_proprietorship_scenario["response_body"],
        "create_merchant_identity_scenario_id": create_identity_individual_sole_proprietorship_scenario["response_id"],


        "create_buyer_identity_scenario_curl_request": create_buyer_identity_scenario["curl_request_body"],
        "create_buyer_identity_scenario_php_request": create_buyer_identity_scenario["php_request_body"],
        "create_buyer_identity_scenario_response": create_buyer_identity_scenario["response_body"],
        "create_buyer_identity_scenario_id": create_buyer_identity_scenario["response_id"],

        "update_identity_scenario_curl_request": update_identity_scenario["curl_request_body"],
        "update_identity_scenario_php_request": update_identity_scenario["php_request_body"],
        "update_identity_scenario_response": update_identity_scenario["response_body"],
        "update_identity_scenario_id": update_identity_scenario["response_id"],

        "fetch_identity_scenario_response": fetch_identity_scenario["response_body"],
        "fetch_identity_scenario_id": fetch_identity_scenario["response_id"],


        "list_identities_scenario_response": list_identities_scenario["response_body"],

        # MERCHANT VERIFICATIONS
        "list_merchant_verifications_scenario_response": list_identities_scenario["response_body"],
        "list_merchant_verifications_platform_user_scenario_response": list_identities_scenario["response_body"],


        # MERCHANTS --------------------------------------------

        "provision_merchant_scenario_curl_request": provision_merchant_scenario["curl_request_body"],
        "provision_merchant_scenario_php_request": provision_merchant_scenario["php_request_body"],
        "provision_merchant_scenario_response": provision_merchant_scenario["response_body"],
        "provision_merchant_scenario_id": provision_merchant_scenario["response_id"],

        "fetch_merchant_scenario_response": fetch_merchant_scenario["response_body"],
        "fetch_merchant_scenario_id": fetch_merchant_scenario["response_id"],

        "reattempt_provision_merchant_scenario_curl_request": reattempt_provision_merchant_scenario["curl_request_body"],
        "reattempt_provision_merchant_scenario_php_request": reattempt_provision_merchant_scenario["php_request_body"],
        "reattempt_provision_merchant_scenario_response": reattempt_provision_merchant_scenario["response_body"],
        "reattempt_provision_merchant_scenario_id": reattempt_provision_merchant_scenario["response_id"],

        "toggle_merchant_processing_scenario_curl_request": toggle_merchant_processing_scenario["curl_request_body"],
        "toggle_merchant_processing_scenario_php_request": toggle_merchant_processing_scenario["php_request_body"],
        "toggle_merchant_processing_scenario_response": toggle_merchant_processing_scenario["response_body"],
        "toggle_merchant_processing_scenario_id": toggle_merchant_processing_scenario["response_id"],

        "toggle_merchant_settlements_scenario_curl_request": toggle_merchant_settlements_scenario["curl_request_body"],
        "toggle_merchant_settlements_scenario_php_request": toggle_merchant_settlements_scenario["php_request_body"],
        "toggle_merchant_settlements_scenario_response": toggle_merchant_settlements_scenario["response_body"],
        "toggle_merchant_settlements_scenario_id": toggle_merchant_settlements_scenario["response_id"],

        "list_merchants_scenario_response": list_merchants_scenario["response_body"],

        # IDENTITY VERIFICATION --------------------------

        # "create_identity_verification_scenario_curl_request": create_identity_verification_scenario["curl_request_body"],
        # "create_identity_verification_scenario_php_request": create_identity_verification_scenario["php_request_body"],
        # "create_identity_verification_scenario_response": create_identity_verification_scenario["response_body"],
        # "create_identity_verification_scenario_id": create_identity_verification_scenario["response_id"],
        #
        # "fetch_identity_verification_scenario_response": fetch_identity_verification_scenario["response_body"],
        # "fetch_identity_verification_scenario_id": fetch_identity_verification_scenario["response_id"],


        # "list_identity_verifications_scenario_curl_request": list_identity_verifications_scenario["curl_request_body"],
        # "list_identity_verifications_scenario_php_request": list_identity_verifications_scenario["php_request_body"],
        # "list_identity_verifications_scenario_response": list_identity_verifications_scenario["response_body"],

        # PAYMENT INSTRUMENTS (cards) --------------------------

        "create_card_scenario_curl_request": create_card_scenario["curl_request_body"],
        "create_card_scenario_php_request": create_card_scenario["php_request_body"],
        "create_card_scenario_response": create_card_scenario["response_body"],
        "create_card_scenario_id": create_card_scenario["response_id"],

        "update_payment_instrument_scenario_curl_request": update_payment_instrument_scenario["curl_request_body"],
        "update_payment_instrument_scenario_php_request": update_payment_instrument_scenario["php_request_body"],
        "update_payment_instrument_scenario_response": update_payment_instrument_scenario["response_body"],
        "update_payment_instrument_scenario_id": update_payment_instrument_scenario["response_id"],

        # "account_updater_scenario_curl_request": account_updater_scenario["curl_request_body"],
        # "account_updater_scenario_php_request": account_updater_scenario["php_request_body"],
        # "account_updater_scenario_response": account_updater_scenario["response_body"],
        # "account_updater_scenario_id": account_updater_scenario["response_id"],


        "fetch_payment_instrument_scenario_response": fetch_payment_instrument_scenario["response_body"],
        "fetch_payment_instrument_scenario_id": fetch_payment_instrument_scenario["response_id"],

        "list_payment_instruments_scenario_response": list_payment_instruments_scenario["response_body"],

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

        "fetch_transfer_scenario_response": fetch_transfer_scenario["response_body"],
        "fetch_transfer_scenario_id": fetch_transfer_scenario["response_id"],

        "list_transfers_scenario_response": list_transfers_scenario["response_body"],

        # # TRANSFERS (Credits) --------------------------------------------

        # "create_credit_scenario_curl_request": create_credit_scenario["curl_request_body"],
        # "create_credit_scenario_php_request": create_credit_scenario["php_request_body"],
        # "create_credit_scenario_response": create_credit_scenario["response_body"],
        # "create_credit_scenario_id": create_credit_scenario["response_id"],

        "create_bank_debit_scenario_curl_request": create_bank_debit_scenario["curl_request_body"],
        "create_bank_debit_scenario_php_request": create_bank_debit_scenario["php_request_body"],
        "create_bank_debit_scenario_response": create_bank_debit_scenario["response_body"],
        "create_bank_debit_scenario_id": create_bank_debit_scenario["response_id"],


       #Push-to-card Scenarios
       "create_recipient_identity_scenario_curl_request": create_recipient_identity_scenario["curl_request_body"],
       "create_recipient_identity_scenario_php_request": create_recipient_identity_scenario["php_request_body"],
       "create_recipient_identity_scenario_response": create_recipient_identity_scenario["response_body"],
       "create_recipient_identity_scenario_id": create_recipient_identity_scenario["response_id"],

       "create_recipient_card_scenario_curl_request": create_recipient_card_scenario["curl_request_body"],
       "create_recipient_card_scenario_php_request": create_recipient_card_scenario["php_request_body"],
       "create_recipient_card_scenario_response": create_recipient_card_scenario["response_body"],
       "create_recipient_card_scenario_id": create_recipient_card_scenario["response_id"],

       "create_recipient_push_to_card_transfer_curl_request": create_recipient_push_to_card_transfer["curl_request_body"],
       "create_recipient_push_to_card_transfer_php_request": create_recipient_push_to_card_transfer["php_request_body"],
       "create_recipient_push_to_card_transfer_response": create_recipient_push_to_card_transfer["response_body"],
       "create_recipient_push_to_card_transfer_id": create_recipient_push_to_card_transfer["response_id"],

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

        "fetch_authorization_scenario_response": fetch_authorization_scenario["response_body"],
        "fetch_authorization_scenario_id": fetch_authorization_scenario["response_id"],

        "void_authorization_scenario_curl_request": void_authorization_scenario["curl_request_body"],
        "void_authorization_scenario_php_request": void_authorization_scenario["php_request_body"],
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
        "create_webhook_scenario_response": create_webhook_scenario["response_body"],
        "create_webhook_scenario_id": create_webhook_scenario["response_id"],

        "fetch_webhook_scenario_response": fetch_webhook_scenario["response_body"],
        "fetch_webhook_scenario_id": fetch_webhook_scenario["response_id"],

        "list_webhooks_scenario_response": list_webhooks_scenario["response_body"],

        # SETTLEMENTS -----------------------------------------------------
        #
        "create_settlement_scenario_curl_request": create_settlement_scenario["curl_request_body"],
        "create_settlement_scenario_php_request": create_settlement_scenario["php_request_body"],
        "create_settlement_scenario_response": create_settlement_scenario["response_body"],
        "create_settlement_scenario_id": create_settlement_scenario["response_id"],


        "fund_settlement_scenario_curl_request": fund_settlement_scenario["curl_request_body"],
        "fund_settlement_scenario_php_request": fund_settlement_scenario["php_request_body"],
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
        "associate_dummyV1_payment_processor_scenario_response": associate_dummyV1_payment_processor_scenario["response_body"],
        "associate_dummyV1_payment_processor_scenario_id": associate_dummyV1_payment_processor_scenario["response_id"],

        # "associate_litleV1_payment_processor_scenario_curl_request": associate_litleV1_payment_processor_scenario["curl_request_body"],
        # "associate_litleV1_payment_processor_scenario_php_request": associate_litleV1_payment_processor_scenario["php_request_body"],
        # "associate_litleV1_payment_processor_scenario_response": associate_litleV1_payment_processor_scenario["response_body"],
        # "associate_litleV1_payment_processor_scenario_id": associate_litleV1_payment_processor_scenario["response_id"],

        "toggle_application_processing_scenario_curl_request": toggle_application_processing_scenario["curl_request_body"],
        "toggle_application_processing_scenario_php_request": toggle_application_processing_scenario["php_request_body"],
        "toggle_application_processing_scenario_response": toggle_application_processing_scenario["response_body"],
        "toggle_application_processing_scenario_id": toggle_application_processing_scenario["response_id"],

        "toggle_application_settlements_scenario_curl_request": toggle_application_settlements_scenario["curl_request_body"],
        "toggle_application_settlements_scenario_php_request": toggle_application_settlements_scenario["php_request_body"],
        "toggle_application_settlements_scenario_response": toggle_application_settlements_scenario["response_body"],
        "toggle_application_settlements_scenario_id": toggle_application_settlements_scenario["response_id"],

        "toggle_on_application_processing_scenario_curl_request": toggle_on_application_processing_scenario["curl_request_body"],
        "toggle_on_application_processing_scenario_php_request": toggle_on_application_processing_scenario["php_request_body"],
        "toggle_on_application_processing_scenario_response": toggle_on_application_processing_scenario["response_body"],
        "toggle_on_application_processing_scenario_id": toggle_on_application_processing_scenario["response_id"],

        "toggle_on_application_settlements_scenario_curl_request": toggle_on_application_settlements_scenario["curl_request_body"],
        "toggle_on_application_settlements_scenario_php_request": toggle_on_application_settlements_scenario["php_request_body"],
        "toggle_on_application_settlements_scenario_response": toggle_on_application_settlements_scenario["response_body"],
        "toggle_on_application_settlements_scenario_id": toggle_on_application_settlements_scenario["response_id"],


        "fetch_application_scenario_response": fetch_application_scenario["response_body"],
        "fetch_application_scenario_id": fetch_application_scenario["response_id"],

        "create_app_scenario_curl_request": create_app_scenario["curl_request_body"],
        "create_app_scenario_php_request": create_app_scenario["php_request_body"],
        "create_app_scenario_response": create_app_scenario["response_body"],
        "create_app_scenario_id": create_app_scenario["response_id"],

        "list_applications_scenario_response": list_applications_scenario["response_body"],

        # TOKENS -------------------------------------------------------
        "create_token_scenario_request": create_token_scenario["request_body"],
        "create_token_scenario_response": create_token_scenario["response_body"],
        "create_token_scenario_id": create_token_scenario["response_id"],

        "associate_token_scenario_curl_request": associate_token_scenario["curl_request_body"],
        "associate_token_scenario_php_request": associate_token_scenario["php_request_body"],
        "associate_token_scenario_response": associate_token_scenario["response_body"],
        "associate_token_scenario_id": associate_token_scenario["response_id"],

        # USERS --------------------------------------------
        "create_owner_user_scenario_curl_request": create_owner_user_scenario["curl_request_body"],
        "create_owner_user_scenario_php_request": create_owner_user_scenario["php_request_body"],
        "create_owner_user_scenario_response": create_owner_user_scenario["response_body"],
        "create_owner_user_scenario_id": create_owner_user_scenario["response_id"],
        "create_owner_user_scenario_password": json.loads(create_owner_user_scenario["response_body"])['password'],

        "create_user_partner_role_scenario_curl_request": create_user_partner_role_scenario["curl_request_body"],
        "create_user_partner_role_scenario_php_request": create_user_partner_role_scenario["php_request_body"],
        "create_user_partner_role_scenario_response": create_user_partner_role_scenario["response_body"],
        "create_user_partner_role_scenario_id": create_user_partner_role_scenario["response_id"],
        "create_user_partner_role_scenario_password": json.loads(create_user_partner_role_scenario["response_body"])['password'],

        "create_user_merchant_role_scenario_curl_request": create_user_merchant_role_scenario["curl_request_body"],
        "create_user_merchant_role_scenario_php_request": create_user_merchant_role_scenario["php_request_body"],
        "create_user_merchant_role_scenario_response": create_user_merchant_role_scenario["response_body"],
        "create_user_merchant_role_scenario_id": create_user_merchant_role_scenario["response_id"],
        "create_user_merchant_role_scenario_password": json.loads(create_user_merchant_role_scenario["response_body"])['password'],

        "disable_user_scenario_curl_request": disable_user_scenario["curl_request_body"],
        "disable_user_scenario_php_request": disable_user_scenario["php_request_body"],
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
        # "update_queued_state_scenario_response": update_queued_state_scenario["response_body"],
        # "update_queued_state_scenario_id": update_queued_state_scenario["response_id"],
        #

    }

    # COMBINE CONFIGS W/ SCENARIO VARs
    template_vars = config_values.copy()
    template_vars.update(api_scenario_vars)
    return template_vars


build_docs()