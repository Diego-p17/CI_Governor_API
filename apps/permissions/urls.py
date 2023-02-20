from rest_framework import routers
from .api           import PermissionViewSet

router = routers.DefaultRouter()

router.register('api/Permissions', PermissionViewSet, 'permissions')

urlpatterns = router.urls