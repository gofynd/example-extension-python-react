from sanic.views import HTTPMethodView
from sanic.response import json as json_response
from fdk_client.platform.PlatformClient import PlatformClient
import ujson


# Get all products
class ProductData(HTTPMethodView):

    async def get(self, request):

        platform_client: PlatformClient = request.conn_info.ctx.platform_client
        response = await platform_client.catalog.getProducts()

        return json_response(response["json"], status=200)

