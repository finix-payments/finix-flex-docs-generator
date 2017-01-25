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

import io.{{api_name_downcase}}.payments.processing.client.ProcessingClient;
import io.{{api_name_downcase}}.payments.processing.client.model.*;

//...

public static void main(String[] args) {

  ProcessingClient client = new ProcessingClient("{{staging_base_url}}");
  client.setupUserIdAndPassword("{{basic_auth_username}}", "{{basic_auth_password}}");

//...
