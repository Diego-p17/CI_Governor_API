from rest_framework import routers
from .api           import TokenViewSet

router = routers.DefaultRouter()

router.register('api/Tokens', TokenViewSet, 'tokens')

urlpatterns = router.urls
