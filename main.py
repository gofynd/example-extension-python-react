import os

from sanic import Sanic
from sanic.response import file, json

from app.factory.boot import startup, shutdown
from app.urls.healthz import health_bp
from app.fdk import get_extension_client 
from app.config import CONFIG

from fdk_extension.extension import FdkExtensionClient

def create_app() -> Sanic:
    fdk_extension_client: FdkExtensionClient = get_extension_client()

    # Sanic Application
    app = Sanic(__name__)

    # health apis
    app.blueprint(health_bp)

    # Add your application routes into platform apis
    from app.urls.application import app_bp
    fdk_extension_client.platform_api_routes.append(app_bp)

    # Register your routes here
    app.blueprint(fdk_extension_client.fdk_route)
    app.blueprint(fdk_extension_client.platform_api_routes)


    # Configure Static Files
    BUILD_DIR = os.path.join(CONFIG.ROOT_DIR, "build")
    if not os.path.exists(BUILD_DIR):
        raise Exception(f"DIST_DIR not found: {BUILD_DIR}, Build FrondEnd before running server!")
    app.static('/', BUILD_DIR)


    # Home Page
    @app.get("/company/<company_id>")
    async def home_page_handler(request, company_id):
        return await file(os.path.join(BUILD_DIR, "index.html"), headers={"Content-Type": "text/html"})

    @app.get("/company/<company_id>/application/<application_id>")
    async def home_page_handler(request, company_id, application_id):
        return await file(os.path.join(BUILD_DIR, "index.html"), headers={"Content-Type": "text/html"})


    # handle webhook
    @app.post("api/v1.0/webhooks")
    async def handle_webbhook(request):
        try: 
            res = await fdk_extension_client.webhook_registry.process_webhook(request)
            print(res)
            return json({"msg": "success"}, status=200)
        except Exception as e:
            return json({"msg": f"err: {str(e)}"}, status=400)
    

    # Boot 
    app.register_listener(startup, "after_server_start")
    app.register_listener(shutdown, "before_server_stop")

    return app