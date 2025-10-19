from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from .models import Event, Family, Genus, Location, Order, Species

ENTRIES_PER_PAGE = 8

def order_list(request):
    order_list = Order.objects.all()
    paginator = Paginator(order_list, ENTRIES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        orders = paginator.page(page_number)
    except PageNotAnInteger:
        # The desired page is not an integer, show the first page
        orders = paginator.page(1)
    except EmptyPage:
        # The desired page is out of range of the actual page count.
        # Show the last page
        orders = paginator.page(paginator.num_pages)
    return render(
        request,
        'birds/order/list.html',
        {'orders': orders}
    )


def family_list(request, order):
    order = get_object_or_404(
        Order,
        slug=order
    )
    family_list = order.families.all()
    paginator = Paginator(family_list, ENTRIES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        families = paginator.page(page_number)
    except PageNotAnInteger:
        # The desired page is not an integer, show the first page
        families = paginator.page(1)
    except EmptyPage:
        # Page number page_number not found, render the last page
        families = paginator.page(paginator.num_pages)
    return render(
        request,
        'birds/family/list.html',
        {
            'order': order,
            'families': families,
        }
    )


def genus_list(request, family):
    family = get_object_or_404(
        Family,
        slug=family
    )
    return render(
        request,
        'birds/genus/list.html',
        {'family': family}
    )


def species_list(request, genus):
    genus = get_object_or_404(
        Genus,
        slug=genus
    )
    return render(
        request,
        'birds/species/list.html',
        {'genus': genus}
    )


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