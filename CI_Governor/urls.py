"""CI_Governor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.organizations.urls')),
    path('', include('apps.generals.urls')),
    path('', include('apps.aplications.urls')),
    path('', include('apps.packageConfig.urls')),
    path('', include('apps.packageConfigKeys.urls')),
    path('', include('apps.devices.urls')),
    path('', include('apps.keys.urls')),
    path('', include('apps.locations.urls')),
    path('', include('apps.peoples.urls')),
    path('', include('apps.permissions.urls')),
    path('', include('apps.settings.urls')),
    path('', include('apps.sites.urls')),
    path('', include('apps.tokens.urls')),
    path('', include('apps.zones.urls')),
    path('', include('apps.login.urls')),
]
