> Example Response:

```json
{{create_user_platform_role_scenario_response}}
```


This is the equivalent of provisioning API keys (i.e. credentials) for a Platform.

<aside class="notice">
A credential with a level of ROLE_PLATFORM has access to all Application and Merchant data.
</aside>


#### HTTP Request

`POST {{staging_base_url}}/users`

#### URL Parameters
Field | Type | Description
----- | ---- | -----------
role | *string*, **required** | Permission level of the user

