import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.lib.Page;
import io.finix.payments.views.*;

Maybe<Page<Authorization>> response = api.authorizations.get();

if (! response.succeeded()) {
   ApiError error = response.error();
   System.out.println(error.getCode());
   System.out.println(error.getMessage());
   System.out.println(error.getDetails());
   throw new RuntimeException("API error attempting to list all Authorizations");
}

 Page<Authorization> page = response.view();
 Page<Authorization> page2 = page.getNext();
