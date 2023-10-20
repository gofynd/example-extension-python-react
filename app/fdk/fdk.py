from app.config import CONFIG
from app.factory.redis import redis_client
from app.fdk.exntension_handlers import ExtensionHandlers
from app.fdk.webhook_handlers import WebhookHandlers

from fdk_extension import setup_fdk
from fdk_extension.extension import FdkExtensionClient
from fdk_extension.storage.redis_storage import RedisStorage


def get_extension_client() -> FdkExtensionClient:
    print(f'dealing with extension client @ {CONFIG.EXTENSION_API_KEY}')

    # extension handlers for callbacks
    extension_handlers = ExtensionHandlers()

    # webhook handlers
    webhook_handlers = WebhookHandlers()

    # setting up the fdk client
    fdk_extension_client = setup_fdk({
        "api_key": CONFIG.EXTENSION_API_KEY,
        "api_secret": CONFIG.EXTENSION_API_SECRET,
        "base_url": CONFIG.EXTENSION_BASE_URL,
        "callbacks": {
            "auth": extension_handlers.auth,
            "uninstall": extension_handlers.uninstall
        },
        "storage": RedisStorage(redis_client, prefix_key="extension-python-vue"),
        "access_mode": "offline",
        "cluster": CONFIG.EXTENSION_CLUSTER_URL,
        # "webhook_config": {
        #     "api_path": "/webhook",
        #     "notification_email": "test2@abc.com",
        #     "subscribed_saleschannel": 'specific',
        #     "event_map": { 
        #         'application/coupon/update': {
        #             "version": '1',
        #             "handler": webhook_handlers.handle_coupon_edit
        #         },
        #         'company/location/update': {
        #             "version": '1',
        #             "handler": webhook_handlers.handle_location_event
        #         },
        #         'company/product/create': {
        #             "version": '1',
        #             "handler": webhook_handlers.handle_product_event
        #         },
        #         'application/product/create': {
        #             "version": '1',
        #             "handler": webhook_handlers.handle_sales_channel_product_event
        #         }
        #     }
        # }
    })

    print("Extension Initiated..!")

    return fdk_extension_client
