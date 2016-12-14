"""charlex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken import views

from charlas.views import (
    UsuarioViewSet,
    OradorViewSet,
    LugarViewSet,
    CharlaViewSet,
    UsuarioCharlaViewSet,
    FotoCharlaViewSet
)

router = routers.SimpleRouter()

router.register(r'usuario', UsuarioViewSet)
router.register(r'orador', OradorViewSet)
router.register(r'lugar', LugarViewSet)
router.register(r'charla', CharlaViewSet)
router.register(r'usuariocharla', UsuarioCharlaViewSet)
router.register(r'fotocharla', FotoCharlaViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
