from rest_framework import routers
from .api           import ConfigurationnViewSet

router = routers.DefaultRouter()

router.register('api/Configurations', ConfigurationnViewSet, 'configurations')

urlpatterns = router.urls