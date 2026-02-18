from re import search

from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView

from resources.forms.resource import ResourcesFilterForm
from resources.models import Resource, Category


# Create your views here.
def resource_list(request):
    resources = Resource.objects.select_related('category', 'location')
    form = ResourcesFilterForm(request.GET or None)

    if form.is_valid():
        search_filter = form.cleaned_data.get('search')
        type_filter=form.cleaned_data.get('type')
        category_filter=form.cleaned_data.get('category')
        location_filter=form.cleaned_data.get('location')

        if search_filter:
            resources = resources.filter(name__icontains=search)
        if type_filter:
            resources = resources.filter(type=type_filter)
        if category_filter:
            resources = resources.filter(category=category_filter)
        if location_filter:
            resources = resources.filter(location=location_filter)

    return render(request, 'resources/catalogue.html', {'resources': resources, 'filter_form': form})


class ResourceDetailView(generic.DetailView):
    model = Resource