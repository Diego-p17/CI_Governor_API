from rest_framework import routers
from .api           import PeopleModuleViewSet

router = routers.DefaultRouter()

router.register('api/PeopleModules', PeopleModuleViewSet, 'peopleModules')

urlpatterns = router.urls