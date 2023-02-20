from rest_framework import routers
from .api           import ZonenViewSet

router = routers.DefaultRouter()

router.register('api/Zones', ZonenViewSet, 'zones')

urlpatterns = router.urls
