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
    protein = forms.IntegerField(required=True)
    fat = forms.IntegerField(required=True)
    sodium = forms.IntegerField(required=True)
    fiber = forms.FloatField(required=True)
    carbs = forms.FloatField(required=True)
    sugars = forms.IntegerField(required=True)


class CerealUpdateForm(forms.Form):
    name = forms.CharField(required=False)
    hctype = forms.CharField(required=False)
    calories = forms.IntegerField(required=False)
    protein = forms.IntegerField(required=False)
    fat = forms.IntegerField(required=False)
    sodium = forms.IntegerField(required=False)
    fiber = forms.FloatField(required=False)
    carbs = forms.FloatField(required=False)
    sugars = forms.IntegerField(required=False)