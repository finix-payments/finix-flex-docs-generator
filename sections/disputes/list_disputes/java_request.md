import io.{{api_name_downcase}}.payments.processing.client.model.Dispute;

transfer.disputeClient().<Resources<Dispute>>resourcesIterator()
  .forEachRemaining(page -> {
    Collection<Dispute> disputes = page.getContent();
  })