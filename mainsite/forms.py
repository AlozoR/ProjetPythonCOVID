from django import forms
from django.contrib.auth.models import User

from .models import Foyer, Produit


class SignInForm(forms.Form):
    username = forms.CharField(label='username', max_length=32)
    nom = forms.CharField(label='nom', max_length=32)
    prenom = forms.CharField(label='prenom', max_length=32)
    mail = forms.CharField(widget=forms.EmailInput, label='mail', max_length=60)
    telephone = forms.CharField(label='telephone', max_length=15)
    adresse = forms.CharField(label='adresse', max_length=100)
    ville = forms.CharField(label='ville', max_length=50)
    mot_de_passe = forms.CharField(widget=forms.PasswordInput, label='mot de passe', max_length=64)
    confirmer_mot_de_passe = forms.CharField(widget=forms.PasswordInput, label='confirmer le mot de passe', max_length=64)
    est_une_residence = forms.ChoiceField(label='type habitat', choices=[('1', 'residence'), ('0', 'maison')])
    habitants = forms.CharField(label='autres habitants', widget=forms.Textarea, max_length=1000, required=False)
    informations_appartement = forms.CharField(label='information_appartement',max_length=50, required=False)

    def clean(self):
        cleaned_data = super(SignInForm, self).clean()
        mot_de_passe = cleaned_data.get('mot_de_passe')
        confirmer_mot_de_passe = cleaned_data.get('confirmer_mot_de_passe')
        telephone = cleaned_data.get('telephone')
        username = cleaned_data.get('username')
        mail = cleaned_data.get('mail')

        if mot_de_passe and confirmer_mot_de_passe:
            if not confirmer_mot_de_passe == mot_de_passe:
                raise forms.ValidationError('Les mots de passe ne sont pas identiques')

        foyers = Foyer.objects.all()
        users = User.objects.all()
        usernames = [u.username for u in users]
        mails = [u.email for u in users]
        tel_foyers = [f.telephone for f in foyers]
        if telephone in tel_foyers:
            raise forms.ValidationError('Ce téléphone est déjà enregistré')

        if username in usernames:
            raise forms.ValidationError('Ce username est déjà enregistré')

        if mail in mails:
            raise forms.ValidationError('Cet email est déja enregistré')

        return cleaned_data


class LogInForm(forms.Form):
    username = forms.CharField(label='username', max_length=32)
    password = forms.CharField(label='mot de passe', widget=forms.PasswordInput)


class CommandeProduitForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CommandeProduitForm, self).__init__(*args, **kwargs)
        produits = Produit.objects.all()
        produits = [p.nom for p in produits if p.est_disponible]
        for p in produits:
            self.fields[p] = forms.BooleanField(initial=False, required=False)

        # for i in BDD:s
        #     field = forms.BooleanField(label=i.name)
        # oeufs = forms.BooleanField(label='oeuf')
        # pates = forms.BooleanField(label='pâtes')
        # sucre = forms.BooleanField(label='sucre')
        # riz = forms.BooleanField(label='riz')
        # huile = forms.BooleanField(label='huile')
        # eau = forms.BooleanField(label='eau')
        # farine = forms.BooleanField(label='farine')
        # papier_toilette = forms.BooleanField(label='papier toilette')
        # savon = forms.BooleanField(label='savon')
        # serviettes = forms.BooleanField(label='serviettes hygiéniques')
        # pack_conserves = forms.BooleanField(label='pack de conserves')
        # gel_hydro = forms.BooleanField(label='gel hydroalcoolique')
        # masques = forms.BooleanField(label='masques')
        # beurre = forms.BooleanField(label='beurre')
        # lait = forms.BooleanField(label='lait')
        # yaourt = forms.BooleanField(label='yaourts')
        # steak = forms.BooleanField(label='steaks hachés')
        # volaille = forms.BooleanField(label='volaille')
        # sel_poivre = forms.BooleanField(label='sel et poivre')
        # charcuterie = forms.BooleanField(label='charcuterie')
        # pack_legumes = forms.BooleanField(label='pack de légumes')
        # pack_fruits = forms.BooleanField(label='pack de fruits')
        # pain = forms.BooleanField(label='pain')
        # vin = forms.BooleanField(label='vin')
        # pack_fromage = forms.BooleanField(label='pack de fromage')
