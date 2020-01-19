from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='trainers'),
    path('<int:trainer_id>', views.trainer, name='trainer'),
]