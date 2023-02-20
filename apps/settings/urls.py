from rest_framework import routers
from .api           import SettingViewSet

router = routers.DefaultRouter()

router.register('api/Settings', SettingViewSet, 'settings')

urlpatterns = router.urls
