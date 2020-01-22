from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Trainer

# Create your views here.
def index(request):
    trainers = Trainer.objects.order_by('first_name')

    paginator = Paginator(trainers, 6)
    page = request.GET.get('page')
    paged_trainers = paginator.get_page(page)


    context = {
        'trainers': paged_trainers
    }
    return render(request, 'trainers/trainers.html', context)

def trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)

    context = {
        'trainer': trainer
    }
    return render(request, 'trainers/trainer.html', context)