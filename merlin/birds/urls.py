from django.urls import path
from . import views

app_name = 'birds'

urlpatterns = [
    #path('', views.events_list, name='events-list'),
    path('', views.EventListView.as_view(), name='events-list'),
    path('event/<int:id>', views.event_detail, name='event-detail'),
    #path('locations/', views.location_list, name='location-list'),
    path('locations/', views.LocationListView.as_view(), name='location-list'),
    path('locations/<slug:location>', views.location_detail, name='location-detail'),
    #path('orders/', views.order_list, name='order-list'),
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    #path('families/<slug:order>', views.family_list, name='family-list'),
    path('families/<slug:order>', views.FamilyListView.as_view(), name='family-list'),
    #path('genuses/<slug:family>', views.genus_list, name='genus-list'),
    path('genuses/<slug:family>', views.GenusListView.as_view(), name='genus-list'),
    path('species/<int:species_id>/', views.species_detail, name='species-detail'),
    #path('species/<slug:genus>', views.species_list, name='species-list'),
    path('species/<slug:genus>', views.SpeciesListView.as_view(), name='species-list'),
]