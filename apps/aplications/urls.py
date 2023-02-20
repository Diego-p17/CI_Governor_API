from rest_framework import routers
from .api           import AplicationViewSet, ModuleViewSet, SectionViewSet

router = routers.DefaultRouter()
router.register( 'api/Aplications', AplicationViewSet, 'aplications')
router.register( 'api/Modules', ModuleViewSet, 'modules')
router.register( 'api/Sections', SectionViewSet, 'sections')

urlpatterns = router.urls
