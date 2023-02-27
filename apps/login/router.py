
from .api import Loginviewsets
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register('api/Login', Loginviewsets, 'login')