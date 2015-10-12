from django import forms
from main.models import Cereal


class CerealForm(forms.ModelForm):
    class Meta:
        model = Cereal
        fields = '__all__'


class CerealForm2(forms.Form):
    name = forms.CharField(required=True)
    hctype = forms.CharField(required=True)
    calories = forms.IntegerField(required=True)


class CerealUpdateForm(forms.Form):
    name = forms.CharField(required=False)
    hctype = forms.CharField(required=False)
    calories = forms.IntegerField(required=False)
