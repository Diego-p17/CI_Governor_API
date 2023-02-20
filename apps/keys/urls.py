from rest_framework import routers
from .api           import KeysViewSet

router = routers.DefaultRouter()

router.register('api/Keys', KeysViewSet, 'keys')

urlpatterns = router.urls