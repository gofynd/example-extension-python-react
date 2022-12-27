from app.config import CONFIG
from main import create_app

from sanic import Sanic
from sanic.worker.loader import AppLoader


is_dev = CONFIG.ENV == "dev"

if __name__ == "__main__":
    loader = AppLoader(factory=create_app)
    app = loader.load()
    app.prepare(
        host="127.0.0.1", 
        port=CONFIG.PORT, 
        auto_reload=False, 
        access_log=is_dev,
        workers=1
    )
    Sanic.serve(primary=app, app_loader=loader)