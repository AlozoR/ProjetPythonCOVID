from django.db import models
from django.contrib.auth.models import User


class Foyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=50)
    est_une_residence = models.BooleanField(default=True)
    telephone = models.CharField(max_length=15, unique=True)
    habitants = models.TextField(max_length=1000)
    informations_appartement = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'Foyer de {self.user.first_name} {self.user.last_name}'
