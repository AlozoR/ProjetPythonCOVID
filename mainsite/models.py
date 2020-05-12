from django.db import models
from django.contrib.auth.models import User


class Foyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.TextField(max_length=100)
    ville = models.TextField(max_length=50)
    est_une_residence = models.BooleanField(default=True)
    habitants = models.TextField(max_length=1000)

    def __str__(self):
        return f'Foyer de {self.user.first_name} {self.user.last_name}'
