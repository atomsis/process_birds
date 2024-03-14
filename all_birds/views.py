from django.shortcuts import render, redirect, get_object_or_404
from .forms import BirdForm
from .models import Bird, BirdSaw
from django.utils import timezone


def bird_list_view(request):
    birds = Bird.objects.all()
    return render(request, 'all_birds/birds_list.html', {'birds': birds})


def bird_detail_view(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'all_birds/bird_detail.html', {'bird': bird})


def create_bird(request):
    if request.method == 'POST':
        form = BirdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bird_list')
    else:
        form = BirdForm()
    return render(request, 'all_birds/create_bird.html', {'form': form})


def mark_bird_sighting(request, bird_id):
    bird = get_object_or_404(Bird, pk=bird_id)
    if 'seen_birds' not in request.session:
        request.session['seen_birds'] = []
    if bird_id not in request.session['seen_birds']:
        request.session['seen_birds'].append(bird_id)
    return redirect('all_birds/bird_detail', bird_id=bird_id)


def seen_birds(request):
    seen_birds = Bird.objects.filter(id__in=request.session.get('seen_birds', []))
    return render(request, 'all_birds/seen_birds.html', {'seen_birds': seen_birds})


def add_sighting(request):
    for bird_id in request.session.get('seen_birds', []):
        bird = Bird.objects.get(id=bird_id)
        sighting = BirdSaw.objects.create(bird=bird)
    request.session['seen_birds'] = []
    return redirect('seen_birds')


def bird_sightings(request):
    sightings = BirdSaw.objects.all()
    return render(request, 'bird_sightings.html', {'sightings': sightings})
