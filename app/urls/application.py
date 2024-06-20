from sanic import Blueprint

from app.views.products import ProductData
from app.views.app_products import AppProductData


# Create your blueprints here
product_bp = Blueprint("product_blueprint", url_prefix="/products")
app_product_bp = Blueprint("app_product_blueprint", url_prefix="/<application_id>/products")

# Register routes into blueprints
product_bp.add_route(ProductData.as_view(), "/")
app_product_bp.add_route(AppProductData.as_view(), "/")



# Blueprint Group
bps = [
    product_bp,
    app_product_bp
]
app_bp = Blueprint.group(*bps, url_prefix="api/v1.0")

