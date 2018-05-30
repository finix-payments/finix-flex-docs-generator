### Webhooks

__Will I receive a request for each event or will we receive them in batch?__  

* You will receive a request for each individual event. For application `Webhooks` you'll receive them for any state change that occurs with an Application. Such as a change in state for a `Transfer`, `Merchant` account provisioning, and Disputes.  

__Is there a specific time at which events will be sent?__  

* Whenever a state change occurs in the database the event will be fired off, thus making them as real-time as possible.  

__Is there a way to tell {{api_name}} that the event was successfully received? What type of response should we send?__  

* Any type of 200 HTTP code will suffice.  


__If the event wasn't received, is it going to be sent again? What type of response/exception should I send?__  

* Yes, if no response from the end-point is received by the `Webhook` it automatically will be replayed.  

__Is {{api_name}} sending any confidential information? I'd like to know if using a public service, like https://requestb.in, for testing the `Webhooks` is an option.__  

* Yes, you can use https://requestb.in to test `Webhooks`. We won't ever send sensitive credit card data, but will return DOBs and addresses. You can review the [sample payloads](#sample-payloads).  

# Events
__Is there a list of all the event types and their payload?__

* Here's a  list of our [webhooks](#sample-payloads)  

__I'll need a way to make sure that the same event is not processed twice, is it possible to include a unique ID in each request?__  

* We currently do not have this capability. It is on the roadmap, but unfortunately we don't have a definitive timeframe.  

__I'll need a way to consolidate our transactions with the information received from the event. Is there a processor transaction ID that will be sent with each event?__  
* Yes, there are resource ID's that are in each response. Examples below:   
1. [Authorization](#created-authorization)  
2. [Transfer (e.g. debit, refund, credit)](#created-new-transfer)  

# Security
__Do I only need to whitelist a single IP?__  
* We submit the requests from multiple IP addresses.  

__How do I validate that Finix is the right caller?__  

* We can provide you a list of the IP addresses where you can expect to receive the events.  

__When I update the URL of a `Webhook` through the API is there a delay before the new URL starts sending events?__  

__Do we need a grace period for the previous URL?__  
* There shouldn't be any delays, but you can actually have multiple webhooks enabled at the same time to prevent any issues for migrating over to a new URL.

__How many retries and at which frequency will you send `Webhooks`?__  
* There are three attempts and it’s put back in the queue.
