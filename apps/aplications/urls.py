from rest_framework import routers
from .api           import AplicationViewSet 

router = routers.DefaultRouter()
router.register( 'api/Aplications', AplicationViewSet, 'aplications')

urlpatterns = router.urls
