from sanic import Blueprint
from sanic.response import json


health_bp = Blueprint("healthz", url_prefix="")


@health_bp.route("/_healthz")
def healthz(request):
    return json("OK")


@health_bp.route("/_readyz")
def readyz(request):
    return json("OK")
