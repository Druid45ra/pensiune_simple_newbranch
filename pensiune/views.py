from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Camera, Rezervare, Contact


class HomeView(TemplateView):
    template_name = "home.html"


class ListareCamereView(ListView):
    model = Camera
    template_name = "camere_list.html"
    context_object_name = "camere"


class RezervareCreateView(CreateView):
    model = Rezervare
    template_name = "rezervare_form.html"
    fields = [
        "camera",
        "data_sosire",
        "data_plecare",
        "nume_client",
        "email_client",
        "telefon",
    ]
    success_url = reverse_lazy("confirmare_rezervare")


class ContactCreateView(CreateView):
    model = Contact
    template_name = "contact.html"
    fields = ["nume", "email", "mesaj"]
    success_url = reverse_lazy("confirmare_contact")


class DespreNoiView(TemplateView):
    template_name = "despre_noi.html"
