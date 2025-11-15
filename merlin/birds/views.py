from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from .forms import NewFamilyForm, NewGenusForm, NewOrderForm, NewSpeciesForm
from .models import Event, Family, Genus, Location, Order, Species

ENTRIES_PER_PAGE = 8


def order_list(request):
    order_list = Order.objects.all()
    paginator = Paginator(order_list, ENTRIES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        orders = paginator.page(page_number)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        if int(page_number) < 1:
            orders = paginator.page(1)
        else:
            orders = paginator.page(paginator.num_pages)
    form = NewOrderForm()
    return render(
        request,
        'birds/order/list.html',
        {
            'orders': orders,
            'form': form,
        }
    )


def family_list(request, order):
    order = get_object_or_404(
        Order,
        slug=order
    )
    family_list = Family.objects.filter(order=order)
    paginator = Paginator(family_list, ENTRIES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        families = paginator.page(page_number)
    except PageNotAnInteger:
        families = paginator.page(1)
    except EmptyPage:
        if int(page_number) < 1:
            families = paginator.page(1)
        else:
            families = paginator.page(paginator.num_pages)
    form = NewFamilyForm()
    return render(
        request,
        "birds/family/list.html",
        {
            'order': order,
            'families': families,
            'form': form,
        }
    )


def genus_list(request, family):
    fam = get_object_or_404(
        Family,
        slug=family
    )
    genus_list = Genus.objects.filter(family=fam)
    paginator = Paginator(genus_list, ENTRIES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        genuses = paginator.page(page_number)
    except PageNotAnInteger:
        genuses = paginator.page(1)
    except EmptyPage:
        if int(page_number) < 1:
            genuses = paginator.page(1)
        else:
            genuses = paginator.page(paginator.num_pages)
    form = NewGenusForm()
    return render(
        request,
        "birds/genus/list.html",
        {
            'family': fam,
            'genuses': genuses,
            'form': form,
        }
    )


def species_list(request, genus):
    the_genus = get_object_or_404(
        Genus,
        slug=genus
    )
    species_list = Species.objects.filter(genus=the_genus)
    paginator = Paginator(species_list, ENTRIES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        species = paginator.page(page_number)
    except PageNotAnInteger:
        species = paginator.page(1)
    except EmptyPage:
        if int(page_number) < 1:
            species = paginator.page(1)
        else:
            species = paginator.page(paginator.num_pages)
    form = NewSpeciesForm()
    return render(
        request,
        "birds/species/list.html",
        {
            'genus': the_genus,
            'species': species,
            'form': form,
        }
    )


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


@require_POST
def new_order(request):
    order = None
    form = NewOrderForm(data=request.POST)
    if form.is_valid():
        order = form.save()
    return render(
        request,
        'birds/order/new_order.html',
        {
            'order': order,
            'form': form,
        }

    )


@require_POST
def new_family(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id
    )
    family = None
    form = NewFamilyForm(data=request.POST)
    if form.is_valid():
        family = form.save(commit=False)
        family.order = order
        family.save()
    return render(
        request,
        'birds/family/new_family.html',
        {
            'order': order,
            'form': form,
            'family': family,
        }
    )
    

@require_POST
def new_genus(request, family_id: int):
    family = get_object_or_404(
        Family,
        id=family_id
    )
    genus = None
    form = NewGenusForm(data=request.POST)
    if form.is_valid():
        genus = form.save(commit=False)
        genus.family = family
        genus.save()
    return render(
        request,
        'birds/genus/new_genus.html',
        {
            'family': family,
            'form': form,
            'genus': genus,
        }
    )


@require_POST
def new_species(request, genus_id: int):
    genus = get_object_or_404(
        Genus,
        id=genus_id
    )
    species = None
    form = NewSpeciesForm(data=request.POST)
    if form.is_valid():
        species = form.save(commit=False)
        species.genus = genus
        species.save()
    return render(
        request,
        'birds/species/new_species.html',
        {
            'genus': genus,
            'form': form,
            'species': species,
        }
    )