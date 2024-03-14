from django.urls import reverse
import pytest
from .models import Bird, BirdSaw

@pytest.fixture
def bird():
    return Bird.objects.create(name='Test Bird', feather_color='Red')

@pytest.fixture
def client():
    from django.test import Client
    return Client()

@pytest.mark.django_db
def test_bird_creation(bird):
    assert Bird.objects.count() == 1
    assert Bird.objects.get(name='Test Bird')

@pytest.mark.django_db
def test_bird_list_view(client, bird):
    response = client.get(reverse('all_birds:bird_list'))
    assert response.status_code == 200
    assert 'Test Bird' in response.content.decode()

@pytest.mark.django_db
def test_bird_detail_view(client, bird):
    response = client.get(reverse('all_birds:bird_detail', args=[bird.id]))
    assert response.status_code == 200
    assert 'Test Bird' in response.content.decode()

@pytest.mark.django_db
def test_mark_bird_sighting(client, bird):
    response = client.get(reverse('all_birds:mark_bird_sighting', args=[bird.id]))
    assert response.status_code == 302

@pytest.mark.django_db
def test_seen_birds_view(client, bird):
    response = client.get(reverse('all_birds:seen_birds'))
    assert response.status_code == 200
    assert 'Test Bird' in response.content.decode()

@pytest.mark.django_db
def test_add_sighting_view(client, bird):
    response = client.post(reverse('all_birds:add_sighting'), {'bird_id': bird.id})
    assert response.status_code == 302

@pytest.mark.django_db
def test_bird_sightings_view(client, bird):
    BirdSaw.objects.create(bird=bird)
    response = client.get(reverse('all_birds:bird_sightings'))
    assert response.status_code == 200
    assert 'Test Bird' in response.content.decode()