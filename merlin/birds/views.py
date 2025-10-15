from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import get_object_or_404, render
from .models import Family, Genus, Order, Species

ENTRIES_PER_PAGE = 8

def order_list(request):
    order_list = Order.objects.all()
    paginator = Paginator(order_list, ENTRIES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    try:
        orders = paginator.page(page_number)
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


def species_detail(request, species, species_id):
    sp = get_object_or_404(
        Species,
        id=species_id,
        slug=species
    )
    print("#############")
    print(sp)
    import os
    print(os.listdir('./birds/templates'))
    print('birds' in os.listdir('./birds/templates'))
    print('species' in os.listdir('./birds/templates/birds'))
    print('detail.html' in os.listdir('./birds/templates/birds/species'))
    print("#############")
    return render(
        request,
        '/birds/species/detail.html',
        {'sp': sp}
    )