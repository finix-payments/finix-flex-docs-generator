import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.enums.BusinessType;
import io.{{api_name_downcase}}.payments.forms.Address;
import io.{{api_name_downcase}}.payments.forms.Date;
import io.{{api_name_downcase}}.payments.forms.IdentityEntityForm;
import io.{{api_name_downcase}}.payments.forms.IdentityForm;
import io.{{api_name_downcase}}.payments.interfaces.ApiError;
import io.{{api_name_downcase}}.payments.interfaces.Maybe;
import io.{{api_name_downcase}}.payments.views.Identity;


IdentityForm form = IdentityForm.builder()
  .entity(IdentityEntityForm.builder()
  .firstName("dwayne")
  .lastName("Sunkhronos")
  .email("user@example.org")
  .businessName("business inc")
  .businessType(BusinessType.LIMITED_LIABILITY_COMPANY)
  .doingBusinessAs("doingBusinessAs")
  .phone("1234567890")
  .businessPhone("+1 (408) 756-4497")
  .taxId("123456789")
  .businessTaxId("123456789")
  .personalAddress(Address.builder()
  .line1("741 Douglass St")
  .line2("Apartment 7")
  .city("San Mateo")
  .region("CA")
  .postalCode("94114")
  .country("USA")
  .build())
  .businessAddress(Address.builder()
  .line1("741 Douglass St")
  .line2("Apartment 7")
  .city("San Mateo")
  .region("CA")
  .postalCode("94114")
  .country("USA")
  .build())
  .dob(Date.builder().day(Integer.valueOf(27)).month(Integer.valueOf(5)).year(Integer.valueOf(1978)).build())
  .maxTransactionAmount(Long.valueOf(1000L))
  .mcc("7399").url("http://sample-entity.com")
  .annualCardVolume(Long.valueOf(100L))
  .defaultStatementDescriptor("Business Inc")
  .incorporationDate(Date.builder().day(Integer.valueOf(1)).month(Integer.valueOf(12)).year(Integer.valueOf(2012)).build())
  .principalPercentageOwnership(Integer.valueOf(51)).build()).build();

Maybe<Identity> response = api.identities.post(form);
if(! response.succeeded().booleanValue()) {
    ApiError error = response.error();
    System.out.println(error.getCode());
    throw new RuntimeException("API error attempting to create Identity");
}
    Identity identity = (Identity)response.view();
    identity.getId();
