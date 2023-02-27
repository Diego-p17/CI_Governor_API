
from .router import router
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]