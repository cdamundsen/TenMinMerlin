from django.urls import path
from . import views

app_name = 'birds'

urlpatterns = [
    path('orders/', views.order_list, name='order_list'),
    path('families/<slug:order>', views.family_list, name='family_list'),
    path('genuses/<slug:family>', views.genus_list, name='genus_list'),
    path('species/<slug:species>/<int:species_id>', views.species_detail, name='species_detail'),
    path('species/<slug:genus>', views.species_list, name='species_list'),
]