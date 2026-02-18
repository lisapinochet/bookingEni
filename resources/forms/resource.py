from django import forms
from resources.models import Resource, Location, Category


class ResourcesFilterForm(forms.Form):
    search = forms.CharField(required=False, label='Rechercher', widget=forms.TextInput(attrs={'placeholder':'Nom de la ressource...'}))

    type = forms.ChoiceField(
        choices=[('', 'Tous les types')] + list(Resource._meta.get_field('type').choices),
        required=False
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label='Toutes les catégories'
    )
    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        required=False,
        empty_label='Tous les lieux'
    )