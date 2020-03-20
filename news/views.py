from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Publication
from django.utils import timezone

def publications_list(request):
    publications = Publication.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')[:5]
    return render(request, 'news/publications_list.html', {'publications':publications})

def create_publication(request):
    return render(request, 'news/create_publication.html')
    
