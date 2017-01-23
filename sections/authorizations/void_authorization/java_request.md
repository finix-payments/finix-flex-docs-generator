Authorization authorization = client.authorizationsClient().fetch(authorization.getId());
authorization.voidMe(true);
