from django.urls import path
from . import views

app_name = 'birds'

urlpatterns = [
    path('', views.EventListView.as_view(), name='events-list'),
    path('event/<int:id>', views.event_detail, name='event-detail'),
    path('locations/', views.LocationListView.as_view(), name='location-list'), 
    path('locations/<slug:location>', views.location_detail, name='location-detail'),
    #path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/', views.order_list, name='order-list'),
    #path('families/<slug:order>', views.FamilyListView.as_view(), name='family-list'),
    path('families/<slug:order>', views.family_list, name='family-list'),
    #path('genuses/<slug:family>', views.GenusListView.as_view(), name='genus-list'),
    path('genuses/<slug:family>', views.genus_list, name='genus-list'),
    path('species/<int:species_id>/', views.species_detail, name='species-detail'),
    #path('species/<slug:genus>', views.SpeciesListView.as_view(), name='species-list'),
    path('species/<slug:genus>', views.species_list, name='species-list'),
    path('new_order/', views.new_order, name='new-order'),
    path('new_family/<int:order_id>', views.new_family, name='new-family'),
    path('new_genus/<int:family_id>', views.new_genus, name='new-genus'),
    path('new_species/<int:genus_id>', views.new_species, name='new-species'),
]