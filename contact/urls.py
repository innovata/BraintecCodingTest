from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from contact import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    re_path(r'^(\w+)_(\w+)/$', views.find, name="find"),
    path("xmlapi/", views.xmlapi, name="xmlapi"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
