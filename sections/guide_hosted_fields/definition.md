## Tokenization with Hosted Fields

### Library summary

The `SecureForm` library is a javascript library that allows you to integrate
secure fields with non-secure fields in your page. The secure fields behave like
traditional input fields while preventing access to the unsecured data.

Once the fields are initialized the library communicates the state of the fields
through a JavaScript callback. The state object includes information about the
validity, focused value and if the user has entered information in the field.

For a complete example of how to use the library please refer to this
[jsFiddle example]({{hosted_fields_jsfiddle}}).

### Step 1: Include library

```html
 <script type="text/javascript" src="{{hosted_fields_src}}"></script>
```

First we'll need to include the library on the webpage where you're hosting your
form. Please include the script as demonstrated to the right.


### Step 2: Initialize the secure form

`SecureForm.create(environment, onUpdateCallback)-> Form`

```javascript

/*
SecureForm.create(environment, onUpdateCallback)-> Form
*/

const secureForm = SecureForm.create('sandbox', function(state) {
   // Logic for interacting with form's potential states
 });
```

The next step is to configure the library. This method is the single entry point into the library.
It initializes and returns a `Form` object representing the secured form.


#### Arguments
Field | Type | Description
----- | ---- | -----------
environment | *string*, **required** |  `sandbox` for testing and `live` for production
onUpdateCallback | *function*, **required** | Callback that will be called whenever the form state changes. It receives the state object representing the current state.

### Step 3: Configure the form fields

`Form#field(selector, properties)-> Field`

```javascript

/*
Form#field(selector, properties)-> Field
*/

secureForm.field('#my-cool-parent', {
    'successColor': '#3c763d',
    'errorColor': '#a94442',
    'lineHeight': '1.5rem',
    'fontSize': '24px',
    'fontFamily': 'Comic Sans',
    'color': '#31708f',
    'placeholder': 'Card number',
    'name': 'cc-number',
    'type': 'card-number',
    'validations': [],
});

```

Now that we have a `Form` object we'll want to style it and add any validations.

#### Arguments
Field | Type | Description
----- | ---- | -----------
selector | *string*, **required** | CSS Selector that points to the element where the field will be added

#### Properties Object
Field | Type | Description
----- | ---- | -----------
name | *string*, **required** | Name of the input field. Will be used when submitting the data.
type | *string*, **required** | Type of the input field (`card-number`, `card-security-code`, `card-expiration-date`, `text`, `password`, `number`, `zip-code`)
validations | *array*, **optional** |  Array of validations that will be used to calculate the `isValid` state (`required`, `validCardExpirationDate`, `validCardNumber`, `validCardSecurityCode`)
placeholder | *string*, **optional** | Text displayed when the field is empty
successColor | *string*, **optional** | Text color when the field is valid
errorColor | *string*, **optional** | Text color when the field is invalid
color | *string*, **optional** | Text color
lineHeight | *string*, **optional** | Line height value
fontSize | *string*, **optional** | Size of text
fontFamily | *string*, **optional** | Font family used in the text.

> Example Response:

```javascript
{
  "number": {
    "isDirty": false,
    "isFocused": false,
    "errorMessages": [
      "is required",
      "is not a valid card number"
    ],
    "isValid": false,
    "name": "number"
  },
  "security_code": {
    "isDirty": false,
    "isFocused": false,
    "errorMessages": [
      "is required",
      "is not a valid security code"
    ],
    "isValid": false,
    "name": "security_code"
  },
  "expiration_month": {
    "isDirty": false,
    "isFocused": false,
    "errorMessages": [
      "is required"
    ],
    "isValid": false,
    "name": "expiration_month"
  },
  "expiration_year": {
    "isDirty": false,
    "isFocused": false,
    "errorMessages": [
      "is required"
    ],
    "isValid": false,
    "name": "expiration_year"
  }
}
```

### Step 4: Submit payload and handle response


`Form#submit(path, options, callback) -> Form
`


```javascript

/*
Form#submit(path, options, callback)-> Form
*/

document.getElementById('cc-form')
  .addEventListener('submit', function(e) {
    e.preventDefault();
    secureForm.submit('/applications/{{create_app_scenario_id}}/tokens', {
        data: {
            type: 'PAYMENT_CARD',
        },
    }, function(status, response) {
        // callback for handling response and sending token to back-end server
        console.log("Response has been received", status, response);
    });
}, false);

```

> Example Response:

```json
{{create_token_scenario_response}}
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
path | *string*, **required** | Path to your `Application's` tokens endpoint
options | *object*, **required** | Options object that can include additional `data`, such as the type of Payment Instrument
callback | *function*, **required** | Callback that will be executed when the HTTPRequest is finished. The callback receives the HTTP status code and the data as two arguments.
