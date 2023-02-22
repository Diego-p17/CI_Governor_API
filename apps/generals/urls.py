from rest_framework import routers
from .api           import *

router = routers.DefaultRouter()

router.register('api/Generals/Country', CountryViewSet, 'countries')
router.register('api/Generals/City', CityViewSet, 'cities')
router.register('api/Generals/DeviceType', DeviceTypeViewSet, 'deviceType')
router.register('api/Generals/HwPlatform', HwPlatformViewSet, 'hwPlatform')
router.register('api/Generals/Os', OsViewSet, 'os')
router.register('api/Generals/TokenType', TokenTypeViewSet, 'tokenType')
router.register('api/Generals/SettingsType', SettingsTypeViewSet, 'settingsType')

urlpatterns = router.urls