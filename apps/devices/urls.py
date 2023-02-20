from rest_framework import routers
from .api           import DeviceViewSet

router = routers.DefaultRouter()

router.register('api/Devices', DeviceViewSet, 'devices')

urlpatterns = router.urls