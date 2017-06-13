import io.finix.payments.ApiClient;
import io.finix.payments.interfaces.ApiError;
import io.finix.payments.interfaces.Maybe;
import io.finix.payments.lib.Page;
import io.finix.payments.views.*;

Maybe<Page<Authorization>> request = api.authorizations.get();

if (! request.succeeded()) {
   ApiError error = request.error();
   System.out.println(error.getCode());
   System.out.println(error.getMessage());
   System.out.println(error.getDetails());
   throw new RuntimeException("API error attempting to list all Authorizations");
}

 Page<Authorization> page = request.view();
 Page<Authorization> page2 = page.getNext();
