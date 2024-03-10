from django.shortcuts import render, redirect, get_object_or_404
from .forms import BirdForm
from .models import Bird, BirdSighting


def bird_list_view(request):
    birds = Bird.objects.all()
    return render(request, 'bird_list.html', {'birds': birds})


def bird_detail_view(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'bird_detail.html', {'bird': bird})


def create_bird_view(request):
    if request.method == 'POST':
        form = BirdForm(request.POST, request.FILES)
        if form.is_valid():
            bird = form.save()
            return redirect('bird_detail', pk=bird.pk)
    else:
        form = BirdForm()
    return render(request, 'create_bird.html', {'form': form})

def bird_sighting_list_view(request):
    sightings = BirdSighting.objects.all()
    return render(request, 'bird_sighting_list.html', {'sightings': sightings})


def mark_bird_sighting_view(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    sighting = BirdSighting.objects.create(bird=bird)
    return redirect('bird_sighting_list')
