from django.urls import path
from . import views

app_name = 'birds'

urlpatterns = [
    path('orders/', views.order_list, name='order-list'),
    path('families/<slug:order>', views.family_list, name='family-list'),
    path('genuses/<slug:family>', views.genus_list, name='genus-list'),
    path('species/<int:species_id>/', views.detail_species, name='detail-species'),
    path('species/<slug:genus>', views.species_list, name='species-list'),
]