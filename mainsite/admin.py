from django.contrib import admin
from .models import Foyer, Commande, Produit
# Register your models here.


admin.site.register([Foyer, Commande, Produit])

