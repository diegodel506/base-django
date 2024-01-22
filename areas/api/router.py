from rest_framework.routers import DefaultRouter
from areas.api.views import AreaApiViewSet

router_area = DefaultRouter()

router_area.register(
    prefix='areas', basename='areas', viewset=AreaApiViewSet
)