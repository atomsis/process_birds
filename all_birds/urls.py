from django.urls import path
from . import views

app_name = 'all_birds'

urlpatterns = [
    path('', views.bird_list_view, name='bird_list'),
    path('bird/<int:bird_id>/', views.bird_detail_view, name='bird_detail'),
    path('bird/create/', views.create_bird, name='create_bird'),
    path('bird/<int:bird_id>/mark_sighting/', views.mark_bird_sighting, name='mark_bird_sighting'),
    path('seen_birds/', views.seen_birds, name='seen_birds'),
    path('add_sighting/', views.add_sighting, name='add_sighting'),
    path('bird_sightings/', views.bird_sightings, name='bird_sightings'),
]
