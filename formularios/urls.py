from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from usuario.views import index, usuario_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^usuario$',usuario_view , name='usuario_crear')
]
