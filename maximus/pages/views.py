from django.shortcuts import render
from django.http import HttpResponse
from sections.models import Section
from trainers.models import Trainer


def index(request):
    sections = Section.objects.order_by('title').filter(is_published=True)
    trainers = Trainer.objects.order_by('first_name')
    context = {
        'sections': sections,
        'trainers': trainers,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    pass