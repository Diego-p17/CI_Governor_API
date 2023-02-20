from rest_framework import routers
from .api           import OrganizationViewSet

router = routers.DefaultRouter()

router.register('api/Organizations', OrganizationViewSet, 'organizations')

urlpatterns = router.urls
