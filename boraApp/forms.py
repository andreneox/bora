from django import forms
from django import forms
from boraApp.models import Lugar

class LugarForm (forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ('nome', 'endereco', 'esporte')

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'autofocus': ''  }),
            'endereco': forms.TextInput(attrs={'class':'form-control'  }),
            'esporte': forms.TextInput(attrs={'class':'form-control'  }),
        }    