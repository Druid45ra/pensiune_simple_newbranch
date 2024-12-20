from django.urls import path
from pensiune import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("camere/", views.ListareCamereView.as_view(), name="camere"),
    path("rezervare/", views.RezervareCreateView.as_view(), name="rezervare"),
    path("contact/", views.ContactCreateView.as_view(), name="contact"),
    path("despre/", views.DespreNoiView.as_view(), name="despre"),
]
