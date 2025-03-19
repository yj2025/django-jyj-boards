from django.contrib import admin
from django.urls import include, path

from pybo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pybo/", include("pybo.urls")),
    path("common/", include("common.urls")), # dev_13
    path("", views.index, name="index"), # dev_13
]
