import io.{{api_name_downcase}}.payments.forms.*;
import io.{{api_name_downcase}}.payments.views.*;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;

Page<Identity> page = api.identities.get().view();
while (page.hasNext()) {
    page = page.getNext();
}