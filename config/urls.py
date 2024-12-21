from django.urls import path, include
from django.contrib import admin
from pensiune import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name="home"),
    path("camere/", views.ListareCamereView.as_view(), name="camere"),
    path("rezervare/", views.RezervareCreateView.as_view(), name="rezervare"),
    path("contact/", views.ContactCreateView.as_view(), name="contact"),
    path("despre/", views.DespreNoiView.as_view(), name="despre"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
