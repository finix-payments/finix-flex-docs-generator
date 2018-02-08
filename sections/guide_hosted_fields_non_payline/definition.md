## Tokenization with Hosted Fields

### Library summary

The `PaymentForm` library is a javascript library that allows you secure your sensitive credit and debit card data. By having the end-user input their data into an iFrame, it prevents third-parties from accessing the information.

Once the fields are initialized the library communicates the state of the fields
through a JavaScript callback. The state object includes information about the
validity, focused value and if the user has entered information in the field.

For a complete example of how to use the library please refer to this
[jsFiddle example]({{hosted_fields_jsfiddle}}).

### Step 1: Include library and desired HTML elements

```html
 <script type="text/javascript" src="{{hosted_fields_src}}"></script>
```

First we'll need to include the library on the webpage where you're hosting your
form. Please include the script as demonstrated to the right.


### Step 2: Initialize the payment form


`window.PaymentForm.card(function(state, binInformation)-> PaymentForm`

```javascript


const paymentForm = window.PaymentForm.card(function(state, binInformation){
     // Logic for interacting with form's potential states (see jsFiddle for  example)
});
```

The next step is to configure the library. This "card" method is the single entry point into the library. It initializes and returns a `PaymentForm` object that contains fields(i.e. name, number, expiration date, & CVV).



### Step 3: Define input fields and configure styling

Now that we have a `PaymentForm` object we'll want to style it

#### DefineField Arguments
Field | Type | Description
----- | ---- | -----------
elementId | *string*, **required** |  Name of HTML id
type | *string*, **required** | API attribute name that will be sent in the payload
placholder | *string*, **required** | What the user will see in the input field


```javascript
function defineField(elementId, type, placeholder) {
  // call field method with desired css styling
  const f = form.field(type, {
    placeholder,
    styles: {
      default: {
        color: "black",
      },
      success: {
        color: '#5cb85c',
      },
      error: {
        color: '#d9534f',
      },
    }
  });
  // appends each field wrapper (that contains placeholder and styles) to the appropriate div
  document.getElementById(elementId).appendChild(f);
}

defineField("field-wrapper-number", "number", '4111 1111 1111 1111');
defineField("field-wrapper-name", "name", 'Bo Jackson');
defineField("field-wrapper-expiration_date", "expiration_date", '02/2020');
defineField("field-wrapper-security_code", "security_code", '411');

```


### Step 4: Submit payload and handle response


`Form#submit(environment, applicationID, callback)-> Form
`


```javascript

/*
Form#submit(environment, applicationID, callback)-> Form
*/

function submitForm() {
  // sandbox or production for environment
  form.submit('sandbox', 'APu7v3CBcRGqh2G5yM52NHPd', function(err, res) {
    if (err) {
      console.log("There was an error");
    }
    // shows id of tokenized payment card
    document.getElementById('preview').innerHTML = JSON.stringify(res, null, '  ');
  })
}

document.getElementById('button').addEventListener('click', function (e){
  e.preventDefault();
  submitForm();
})

// if user types "enter" instead of clicking submit button
form.onSubmit(submitForm);

```

> Example Response:

```json
{
  "status": 201,
  "statusText": "Created",
  "data": {
    "id": "TKiu6N8r5wN38J1xXdeNjzZY",
    "fingerprint": "FPR-2083311660",
    "created_at": "2017-08-29T06:25:54.29Z",
    "updated_at": "2017-08-29T06:25:54.29Z",
    "instrument_type": "PAYMENT_CARD",
    "expires_at": "2017-08-30T06:25:54.29Z",
    "currency": "USD"
  }
}
{
  "cardBrand": "visa",
  "bin": "411111"
}
```


Finally we will need to register a click event that fires when our users submit
the form and define a callback for handling the response.

Next, configure the library to your specific `Application` where all of the form
fields will be submitted during the executed `POST` request. We'll also want to
register a click event that fires when our users submit the form and define a
callback for handling the response.

Once you've handled the response you will want to store that ID to utilize
the token in the future. To do this you will need to send the ID from your
front-end client to your back-end server.


#### Arguments
Field | Type | Description
----- | ---- | -----------
environment | *string*, **required** | `sandbox` for testing and `production` for production
applicationId | *string*, **required** | `Application` id that the payment card will be scoped to
callback | *function*, **required** | Callback that will be executed when the HTTPRequest is finished.
