These guides provide a collection of resources for utilizing the {{api_name}} API and its client libraries. We offer a number of client libraries for interfacing with the API, and you can view example code snippets for each in the dark area to the right.

1. [Quickstart](#quickstart): A step-by-step guide demonstrating the basic workflow of charing a card. This guide will walk you through provisioning merchant accounts, tokenizing cards, charging those cards, and finally settling (i.e. payout) those funds out to your merchants.

2. [Tokenization.js](#tokenization-js): This guide explains how to properly tokenize cards in production via our javascript client to remain out of PCI scope


## Authentication

To communicate with the {{api_name}} API you'll need to authenticate your requests with a `username` and `password`. To test the API against the sandbox environment feel free to use the credentials below:

- Username: `{{basic_auth_username}}`

- Password: `{{basic_auth_password}}`

You should also know your `Application` ID. An `Application`, also referred as an "App", is a resource that represents your web app. In other words, any web service that connects buyers (i.e. customers) and sellers (i.e. merchants). This guide uses the following sandbox `Application` ID:

- App ID: `{{create_app_scenario_id}}`




