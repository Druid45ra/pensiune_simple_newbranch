from django.db import models


class Camera(models.Model):
    TIPURI_CAMERA = [
        ("single", "Single"),
        ("double", "Double"),
        ("suite", "Suite"),
    ]

    numar = models.IntegerField(unique=True)
    tip = models.CharField(max_length=10, choices=TIPURI_CAMERA)
    pret = models.DecimalField(max_digits=6, decimal_places=2)
    descriere = models.TextField(blank=True)

    def __str__(self):
        return f"Camera {self.numar} - {self.tip}"


class Rezervare(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    data_sosire = models.DateField()
    data_plecare = models.DateField()
    nume_client = models.CharField(max_length=100)
    email_client = models.EmailField()
    telefon = models.CharField(max_length=15)

    def __str__(self):
        return f"Rezervare {self.camera} - {self.data_sosire}"


class Contact(models.Model):
    nume = models.CharField(max_length=100)
    email = models.EmailField()
    mesaj = models.TextField()
    data_trimitere = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mesaj de la {self.nume}"
