## Embedded Tokenization

Our embedded tokenization form ensures you remain out of PCI scope, while providing
your end-users with a sleek, and seamless checkout experience.

With our form, sensitive card data never touches your servers and keeps you out
of PCI scope by sending this info over SSL directly to {{api_name}}. For your
convenience we've provided a [jsfiddle]({{embedded_iframe_jsfiddle}}) as a live example.

<aside class="notice">
Note you must still use SSL on your servers for any actions related to financial transactions via the {{api_name}} API.
</aside>

### Step 1: Create a Button

```html
<!DOCTYPE html>
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <body>
        <button id="show-form">Add Your Card</button>
    </body>
</html>
```

Before collecting the sensitive payment information, we will need to add a button
to the HTML where we'll be hosting the iframe so that end-users can input their
details.

We have provided a simple example to the right.


### Step 2: Include library

To use the iframe you will need to include the library on the webpage
where you're hosting the aforementioned button. Please include the script as demonstrated to the right. Please refrain from hosting the iframe library locally as doing so prevents important updates.


```html
<script type="text/javascript" src="{{embedded_iframe_src}}"></script>
```


### Step 3: Configure the client

```javascript
<script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function(event) {
      document.getElementById('show-form').addEventListener('click', function() {
        document.openTokenizeCardForm({
          applicationName: 'Business Name',
          applicationId: '{{create_app_scenario_id}}',
          environment: 'sandbox',
        }, function (tokenizedResponse) {
          // Define a callback to send your token to your back-end server
        });
      });
    });
 </script>
```


Next we need to configure the client so that it associates the card with your `Application`. We will also need to register a click event that fires when our users click on the button, thereby rendering the iframe on the page. Then when the form is submitted you'll be returned a unique `Token` resource representing the submitted card details. We will also need to define a callback for handling that response.

<aside class="notice">
 When you're ready to tokenize in live, pass `live` for the `environment` attribute.
</aside>


In the next step we'll show you how to claim the instrument via an authenticated HTTPS request on your back-end for future use.

> Example Response:

```json
{{create_token_scenario_response}}
```
