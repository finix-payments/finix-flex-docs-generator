/*
Add the following to your pom.xml (Maven file):

<dependency>
  <groupId>{{java_group_id}}</groupId>
  <artifactId>{{java_artifact_id}}</artifactId>
  <version>{{version}}</version>
</dependency>

...

<repositories>
  <repository>
      <id>ossrh</id>
      <url>https://oss.sonatype.org/content/repositories/</url>
      <snapshots>
          <enabled>true</enabled>
      </snapshots>
  </repository>
</repositories>

*/

import io.{{api_name_downcase}}.payments.ApiClient;
import io.{{api_name_downcase}}.payments.views.*;
import io.{{api_name_downcase}}.payments.forms.*;

//...

public static void main(String[] args) {

  ApiClient api = ApiClient.builder()
                  .url("{{staging_base_url}}")
                  .user("{{basic_auth_username_payouts}}")
                  .password("{{basic_auth_password_payouts}}")
                  .build();
//...
