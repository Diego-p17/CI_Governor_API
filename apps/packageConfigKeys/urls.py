from rest_framework import routers
from .api           import PackageConfigKeysViewSet

router = routers.DefaultRouter()

router.register('api/PackageConfigKeys', PackageConfigKeysViewSet, 'packageConfigKeys')

urlpatterns = router.urls