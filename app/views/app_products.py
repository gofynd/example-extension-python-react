from sanic.views import HTTPMethodView
from sanic.response import json as json_response
from fdk_client.platform.PlatformClient import PlatformClient
import ujson


# Get all products
class AppProductData(HTTPMethodView):

    async def get(self, request, application_id: int):

        platform_client: PlatformClient = request.conn_info.ctx.platform_client
        response = await platform_client.application(application_id).catalog.getAppProducts()

        return json_response(response["json"], status=200)

