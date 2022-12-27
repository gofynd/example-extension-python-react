from sanic import Blueprint

from app.views.application import ApplicationData


# Application Blueprint
application_bp = Blueprint("application_blueprint", url_prefix="/applications")
application_bp.add_route(ApplicationData.as_view(), "/")



# Blueprint Group
bps = [
    application_bp
]
app_bp = Blueprint.group(*bps, url_prefix="api/v1.0")

