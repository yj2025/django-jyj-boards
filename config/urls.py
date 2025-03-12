from django.contrib import admin
from django.urls import include, path

from pybo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pybo/", include("pybo.urls")),
]
