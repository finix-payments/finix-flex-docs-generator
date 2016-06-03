import shutil
import os
import glob


def make_scenarios():
    # this provides the ordering for the docs by section and individual snippet
    snippets_by_resource = {
        "guides": [
            "definition",
            "getting_started",
            "create_merchant_identity",
            "create_bank_account",
            "perform_identity_verification",
            "provision_merchant",
            "create_buyer_identity",
            "create_card",
            "create_card_debit",
            "refund_debit",
            "settle_funds",
            ],
        "tokenization": [
            "definition",
            ],
        "authorizations": [
            "definition",
            "create_authorization",
            "capture_authorization",
            "fetch_authorization",
            # "list_authorizations"
        ],

        "disputes": [
            "definition",
            # "create_dispute",
            "fetch_dispute",
            # "list_disputes"
        ],

        "identities": [
            "definition",
            "create_buyer_identity",
            "create_merchant_identity",
            "fetch_identity",
            # # "list_identities",
            # # "list_merchants",
            "underwrite_identity"
        ],

        "identity_verifications": [
            "definition",
            "create_identity_verification",
            "fetch_identity_verification",
            # "list_identity_verifications"
        ],

        "settlements": [
            "definition",
            "create_settlement",
            "fetch_settlement",
            # "list_settlements"
        ],

        "transfers": [
            "definition",
            "create_debit",
            "create_refund",
            "fetch_transfer",
            # "list_transfers"
        ],

        "webhooks": [
            "definition",
            "create_webhook",
            "fetch_webhook",
            # "list_webhooks"
        ],

        "payment_instruments": [
            "definition",
            "create_card",
            "create_bank_account",
            "fetch_payment_instrument",
            "list_payment_instruments"
        ],
        }


    # Determine which client libraries to include
    clients = [
        "curl",
        "php"
        ]

    outfile = os.getcwd() + '/slate_template.md'
    f = open(outfile, 'r+')
    f.truncate()


    file_ordering = [] # all the file will be inserted into this array according to their ordering
    snippet_directory_location = os.getcwd()

    file = snippet_directory_location + "/sections/slate_configs.md"
    file_ordering.append(file)

    # This is the order that the directories / guides will be concatinated
    resources = [
        "guides",
        "tokenization",
        "authorizations",
        "disputes",
        "identities",
        "identity_verifications",
        "settlements",
        "transfers",
        "webhooks",
        "payment_instruments"
    ]

    for resource in resources:
        # iterate over the snippets in the resource directory
        for snippet in snippets_by_resource[resource]:

            if snippet == "definition":
                file = snippet_directory_location + "/sections/" + resource + "/" + snippet + ".md"
                file_ordering.append(file)
            else:
                # add the definition for the specific snippet
                file = snippet_directory_location  + "/sections/" + resource + "/" + snippet + "/definition.md"
                file_ordering.append(file)

                # include all the requests for the specific libraries
                for client in clients:
                    file = snippet_directory_location  + "/sections/client_header/" + client + ".md"
                    file_ordering.append(file)
                    file = snippet_directory_location  + "/sections/" + resource + "/" + snippet + "/" + client + "_request.md"
                    file_ordering.append(file)
                    file = snippet_directory_location  + "/sections/client_header/close_parens.md"
                    file_ordering.append(file)
                # add the response for the snippet
                file = snippet_directory_location  + "/sections/" + resource + "/" + snippet + "/response.md"
                file_ordering.append(file)


    with open(outfile, 'a') as outfile:
        outfile.truncate()
        for fname in file_ordering:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
            outfile.write("\n")

if __name__ == '__main__':
    make_scenarios()