from rest_framework import routers
from .api           import PackageConfigViewSet

router = routers.DefaultRouter()

router.register('api/PackageConfig', PackageConfigViewSet, 'packageConfig')

urlpatterns = router.urls