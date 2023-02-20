from rest_framework import routers
from .api           import SiteViewSet

router = routers.DefaultRouter()

router.register('api/Sites', SiteViewSet, 'sites')

urlpatterns = router.urls
