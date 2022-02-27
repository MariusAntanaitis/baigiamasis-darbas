from django.forms import ModelForm
from pradziamokslis.models import Mokinys


class MokinysForm(ModelForm):
    class Meta:
        model = Mokinys
        fields = ['vardas', 'pavarde', 'email', 'telefono_numeris']

