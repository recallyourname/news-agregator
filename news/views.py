from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Publication
from django.utils import timezone

def publication_view(request, pk):
    publication = Publication.objects.get(pk=pk)
    return render(request, 'news/show_publication.html', {'publication':publication})

class publications_list(ListView):
    model = Publication
    template_name = 'news/publications_list.html'
    context_object_name = 'publications'
    ordering = ['-published_date']
    paginate_by = 5

def create_publication(request):
    return render(request, 'news/create_publication.html')
