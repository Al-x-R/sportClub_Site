from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sections'),
    path('<int:section_id>', views.section, name='section'),
]