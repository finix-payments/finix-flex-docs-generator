transfer = {{ruby_client_resource_name}}::Transfer.retrieve(:id=> "{{create_sender_push_to_card_transfer_id}}")

refund = transfer.reverse(100)
