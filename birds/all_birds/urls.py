from django.urls import path
from .views import *

app_name = 'birds'

urlpatterns = [
    path('', bird_list_view, name='bird_list'),
    path('birds/<int:bird_id>/', bird_detail_view, name='bird_detail'),
    path('birds/create/', create_bird_view, name='create_bird'),
    path('bird-sightings/', bird_sighting_list_view, name='bird_sighting_list'),
    path('bird-sightings/mark/<int:bird_id>/', mark_bird_sighting_view, name='mark_bird_sighting'),
]