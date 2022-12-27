class WebhookHandlers:

    async def handle_coupon_edit(self, event_name, payload, company_id, application_id):
        print(f"Event {event_name} received for {company_id} and {application_id}")
        print(f"Payload: {payload} for {event_name}")

    async def handle_location_event(self, event_name, payload, company_id, application_id):
        print(f"Event {event_name} received for {company_id} and {application_id}")
        print(f"Payload: {payload} for {event_name}")
    
    async def handle_product_event(self, event_name, payload, company_id, application_id):
        print(f"Event {event_name} received for {company_id} and {application_id}")
        print(f"Payload: {payload} for {event_name}")

    async def handle_sales_channel_product_event(self, event_name, payload, company_id, application_id):
        print(f"Event {event_name} received for {company_id} and {application_id}")
        print(f"Payload: {payload} for {event_name}")