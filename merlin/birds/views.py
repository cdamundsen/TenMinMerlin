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


def events_list(request):
    events_list = Event.objects.all()
    paginator = Paginator(events_list, ENTRIES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        events = paginator.page(page_number)
    except PageNotAnInteger:
        # The desired page is not an integer, show the first page
        events = paginator.page(1)
    except EmptyPage:
        # The desired page is out of range of the actual page count.
        # Show the last page
        events = paginator.page(paginator.num_pages)
    return render(
        request,
        'birds/events/list.html',
        {'events': events}
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


def location_list(request):
    locations_list = Location.objects.all()
    paginator = Paginator(locations_list, ENTRIES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        locations = paginator.page(page_number)
    except PageNotAnInteger:
        # The desired page is not an integer, show the first page
        locations = paginator.page(1)
    except EmptyPage:
        # The desired page is out of range of the actual page count.
        # Show the last page
        locations = paginator.page(paginator.num_pages)
    return render(
        request,
        'birds/locations/list.html',
        {'locations': locations}
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