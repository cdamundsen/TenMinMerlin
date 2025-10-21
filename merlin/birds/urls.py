from django.urls import path
from . import views

app_name = 'birds'

urlpatterns = [
    path('', views.EventListView.as_view(), name='events-list'),
    path('event/<int:id>', views.event_detail, name='event-detail'),
    path('locations/', views.LocationListView.as_view(), name='location-list'), 
    path('locations/<slug:location>', views.location_detail, name='location-detail'),
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('families/<slug:order>', views.FamilyListView.as_view(), name='family-list'),
    path('genuses/<slug:family>', views.GenusListView.as_view(), name='genus-list'),
    path('species/<int:species_id>/', views.species_detail, name='species-detail'),
    path('species/<slug:genus>', views.SpeciesListView.as_view(), name='species-list'),
]