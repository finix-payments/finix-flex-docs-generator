import io.{{api_name_downcase}}.payments.views.Authorization;

<!-- Authorization authorization = null;
        authorization = api.authorizations
                .id("{{fetch_authorization_scenario_id}}")
                .get()
                .view();
 -->
Authorization authorization = api.authorizations
                .id("{{fetch_authorization_scenario_id}}")
                .get()
                .view();
