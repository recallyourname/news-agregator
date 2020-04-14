from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Publication
from django.utils import timezone


def publication_view(request, pk):
    publication = Publication.objects.get(pk=pk)
    return render(request, 'news/show_publication.html', {'publication':publication})

def publications_list(request):
    publications = Publication.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')[:5]
    return render(request, 'news/publications_list.html', {'publications':publications})

def create_publication(request):
    return render(request, 'news/create_publication.html')
    
