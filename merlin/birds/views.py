from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Event, Family, Genus, Location, Order, Species

ENTRIES_PER_PAGE = 8

class OrderListView(ListView):
    queryset = Order.objects.all()
    context_object_name = 'orders'
    paginate_by = ENTRIES_PER_PAGE
    template_name = 'birds/order/list.html'


class FamilyListView(ListView):
    model = Family
    context_object_name = 'families'
    paginate_by = ENTRIES_PER_PAGE
    template_name='birds/family/list.html'

    def get_queryset(self):
        return Family.objects.filter(order__slug=self.kwargs['order'])


class GenusListView(ListView):
    model = Genus
    context_object_name = 'genuses'
    paginate_by = ENTRIES_PER_PAGE
    template_name = 'birds/genus/list.html'

    def get_queryset(self):
        return Genus.objects.filter(family__slug=self.kwargs['family'])


class SpeciesListView(ListView):
    model = Species
    context_object_name = 'species'
    paginate_by = ENTRIES_PER_PAGE
    template_name = 'birds/species/list.html'

    def get_queryset(self):
        return Species.objects.filter(genus__slug=self.kwargs['genus'])


class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    paginate_by = ENTRIES_PER_PAGE
    template_name = 'birds/events/list.html'


class LocationListView(ListView):
    model = Location
    context_object_name = 'locations'
    paginate_by = ENTRIES_PER_PAGE
    template_name = 'birds/locations/list.html'


def species_detail(request, species_id):
    sp = get_object_or_404(
        Species,
        id=species_id,
    )
    return render(
        request,
        'birds/species/detail.html',
        {'sp': sp}
    )


def event_detail(request, id):
    event = get_object_or_404(
        Event,
        id=id
    )
    return render(
        request,
        'birds/events/detail.html',
        {'event': event}
    )


def location_detail(request, location):
    loc = get_object_or_404(
        Location,
        slug=location
    )
    return render(
        request,
        'birds/locations/detail.html',
        {'location': loc}
    )