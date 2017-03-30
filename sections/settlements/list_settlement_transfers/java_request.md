Settlement settlement = client.settlementsClient().fetch("{{fetch_settlement_scenario_id}}");
    settlement.transfersClient().<Resources<Transfer>>resourcesIterator()
      .forEachRemaining(page -> {
        Collection<Transfer> transfers = page.getContent();
        transfers.forEach(transfer ->
       // do something
        );
      });
  }


