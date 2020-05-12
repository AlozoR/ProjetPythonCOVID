from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(label='username', max_length=32)
    nom = forms.CharField(label='nom', max_length=32)
    prenom = forms.CharField(label='prenom', max_length=32)
    mail = forms.CharField(label='mail', max_length=60)
    telephone = forms.CharField(label='mail', max_length=60)
    adresse = forms.CharField(label='mail', max_length=60)
    ville = forms.CharField(label='mail', max_length=60)
    mot_de_passe = forms.CharField(label='mail', max_length=60)
    confirmer_mot_de_passe = forms.CharField(label='mail', max_length=60)
    est_une_residence = forms.ChoiceField(choices=('maison', 'residence'))

