# Webhooks

`Webhooks` allow you to build or set up integrations which subscribe to certain
automated notifications (i.e. events) on the {{api_name}} API. When one of those
events is triggered, we'll send a HTTP POST payload to the webhook's configured
URL. Instead of forcing you to pull info from the API, webhooks push notifications to
your configured URL endpoint. `Webhooks` are particularly useful for updating
asynchronous state changes in `Transfers`, `Merchant` account provisioning, and
listening for notifications of newly created `Disputes`.

In v2 of the settlement engine, the `destination` attribute will be deprecated from the Settlement `Webhook` event. The `destination` field will be returned in the transfer (type = created; entity = transfer) `Webhook` event.
