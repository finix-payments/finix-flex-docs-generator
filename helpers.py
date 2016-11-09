import os
import pprint
import poster
import time
import random
import string
import base64
from urllib2 import Request, urlopen, HTTPError
import json
import finix

def formatted_response(endpoint, values, encoded_auth, request_type=None):
    headers = {
        'Content-Type': 'application/vnd.json+api',
        'Authorization': 'Basic ' + encoded_auth
    }
    request = Request(endpoint, data=values, headers=headers)

    # Check if a PUT request
    if request_type is not None:
        request.get_method = lambda: 'PUT'
    try:
        response_body = urlopen(request).read()
    except HTTPError as e:
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

    return string


def format_php_request_body(string):
    string = string.replace("{", "array(")
    string = string.replace("}", ")")
    string = string.replace(":", "=>")
    return string

def format_python_request_body(string):
    string = string.replace("true", "True")
    string = string.replace("false", "False")
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
    names = ["Jim", "Bob", "Joe", "Walter", "Daphne", "Maggie", "Fran",
                    "Jessie", "Michae", "Marcie", "Ricardo", "Amy", "Sean",
                    "Marshall", "Laura", "Collen", "Alex", "Ayisha", "Step"]
    return random.choice (names)

def random_last_name():
    names = ["Jones", "Sterling", "Lopez", "Serna", "Wade", "James", "Curry",
             "Green", "White", "Le", "Kline", "Henderson", "Diaz", "Chang"]
    return random.choice (names)


def format_included_client_header(included_clients):
    string = ""
    for client in included_clients:
        string = string + "- " + included_clients[client]  + ": " + client+ "\n"
    return string
