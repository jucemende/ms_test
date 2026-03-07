"""ms_test URL Configuration."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/clientes/", include("clientes.urls")),
]
