import os
import pprint
import poster
import time
import random
import string
import base64
from urllib2 import Request, urlopen, HTTPError, URLError, build_opener, HTTPHandler
import json
# import finix
import time
# from slacker import Slacker

def formatted_response(endpoint, values, encoded_auth, request_type=None):

    headers = {
        'Content-Type': 'application/vnd.json+api',
        'Authorization': 'Basic ' + encoded_auth
    }

    request = Request(endpoint, data=values, headers=headers)

    opener = build_opener(HTTPHandler(debuglevel=1))
    # Check if a PUT request
    if request_type == "PUT":
        request.get_method = lambda: 'PUT'

    elif request_type == "DELETE":

        request.get_method = lambda: 'DELETE'
        return {'request_body': values,
        'curl_request_body': values}

    elif request_type == "PATCH":
        request.get_method = lambda: 'PATCH'

    try:

        response_body = opener.open(request).read()
    except URLError as e:
        import ipdb; ipdb.set_trace()
        json.loads(e.read())


    if "id" not in json.loads(response_body):
        return {'request_body': values,
                'response_body': response_body,
                }
    response_id = json.loads(response_body)["id"]

    if values:
        return {'request_body': values,
                'curl_request_body': values,
                'php_request_body': format_php_request_body(values),
                'python_request_body': format_python_request_body(values),
                'ruby_request_body': format_ruby_request_body(values),
                'response_body': response_body,
                'response_id': response_id}
    else:
        print 'hit here 3'
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
    return string

def transfer_ready_to_settle(endpoint, encoded_auth):
    values = None

    headers = {
        'Content-Type': 'application/vnd.json+api',
        'Authorization': 'Basic ' + encoded_auth
    }
    request = Request(endpoint, data=values, headers=headers)
    opener = build_opener(HTTPHandler(debuglevel=1))
    response_body = opener.open(request).read()
    return json.loads(response_body)['ready_to_settle_at'] is not None

# def message_slack(channel, message):
#     slack = Slacker('xoxb-216066206390-2V98aTCIppQuMKAkUoWAe3Ad')
#     # Send a message to #general channel
#     slack.chat.post_message(channel, message, as_user="richies_revenge")


def stringified_elapsed_time(start_time):
    m, s = divmod(time.time() - start_time, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def format_php_request_body(string):
    string = string.replace("{", "array(")
    string = string.replace("}", ")")
    string = string.replace(":", "=>")
    return string

def format_python_request_body(string):
    string = string.replace("true", "True")
    string = string.replace("false", "False")
    return string

def format_ruby_request_body(string):
    string = string.replace(":", "=>")
    return string

def random_app_name():
    pay_facs = ["HyperWallet", "Venmo", "Square", "Paypal", "Dwolla", "WePay", "Facebook", "Google", "BrainTree"]
    return random.choice (pay_facs)

def random_business_name():
    BusinessList = ["Bobs Burgers", "Prestige World Wide", "Golds Gym", "Petes Coffee",
                    "Pollos Hermanos", "Lees Sandwiches", "Dunder Mifflin",
                    "Pawny City Hall", "ACME Anchors"]
    return random.choice (BusinessList)


def random_first_name():
    names = ["Jim", "Bob", "Joe", "Walter", "Daphne",
                     "Marcie", "Ricardo", "Amy", "Sean",
                    "Michael", "Laura", "Collen", "Alex", "Ayisha", "Steph"]
    return random.choice (names)

def random_last_name():
    names = ["Jones", "Sterling", "Lopez", "Serna", "Wade", "James", "Curry",
             "Green", "White", "Le", "Kline", "Henderson", "Diaz", "Chang"]
    return random.choice (names)


def format_included_client_header(included_clients):
    if "cURL" in included_clients:
        string = "- " + included_clients["cURL"]  + ": " + "cURL" + "\n"
        included_clients.pop('cURL', None)
    else:
        string = ""
    for client in included_clients:
        string = string + "- " + included_clients[client]  + ": " + client+ "\n"
    return string
