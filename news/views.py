from django.shortcuts import render
from .models import Publication
from django.utils import timezone

def publications_list(request):
    publications = Publication.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'news/publications_list.html', {'publications':publications})