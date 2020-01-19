from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Section

# Create your views here.
def index(request):
    sections = Section.objects.order_by('title').filter(is_published=True)

    paginator = Paginator(sections, 6)
    page = request.GET.get('page')
    paged_sections = paginator.get_page(page)


    context = {
        'sections': paged_sections
    }
    return render(request, 'sections/sections.html', context)

def section(request, section_id):
    section = get_object_or_404(Section, pk=section_id)

    context = {
        'section': section
    }
    return render(request, 'sections/section.html', context)