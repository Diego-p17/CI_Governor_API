from rest_framework import routers
from .api           import AplicationViewSet, SectionViewSet

router = routers.DefaultRouter()
router.register( 'api/Aplications', AplicationViewSet, 'aplications')
router.register( 'api/Sections', SectionViewSet, 'sections')

urlpatterns = router.urls
