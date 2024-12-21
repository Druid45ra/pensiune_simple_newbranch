# Generated by Django 5.1.4 on 2024-12-21 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numar', models.IntegerField(unique=True)),
                ('tip', models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('suite', 'Suite')], max_length=10)),
                ('pret', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descriere', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mesaj', models.TextField()),
                ('data_trimitere', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rezervare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_sosire', models.DateField()),
                ('data_plecare', models.DateField()),
                ('nume_client', models.CharField(max_length=100)),
                ('email_client', models.EmailField(max_length=254)),
                ('telefon', models.CharField(max_length=15)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensiune.camera')),
            ],
        ),
    ]