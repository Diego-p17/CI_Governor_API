from rest_framework import routers
from .api           import PeopleViewSet

router = routers.DefaultRouter()

router.register('api/Peoples', PeopleViewSet, 'peoples')

urlpatterns = router.urls