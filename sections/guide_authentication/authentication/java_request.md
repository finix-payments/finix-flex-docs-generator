/*
Add the following to your pom.xml (Maven file):

<dependency>
  <groupId>io.{{api_name_downcase}}.payments.processing.client</groupId>
  <artifactId>{{java_artifact_id}}</artifactId>
  <version>${version}</version>
</dependency>

...

<repositories>
  <repository>
    <id>oss-snapshots</id>
    <url>https://oss.sonatype.org/content/repositories/snapshots</url>
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
                  .user("{{basic_auth_username}}")
                  .password("{{basic_auth_password}}")
                  .build();
//...


