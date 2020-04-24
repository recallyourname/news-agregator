from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView, UpdateView
)
from .models import Publication
from django.utils import timezone

class publications_list(ListView):
    model = Publication
    template_name = 'news/publications_list.html'
    context_object_name = 'publications'
    ordering = ['-published_date']
    paginate_by = 5

class publication_view(DetailView):
    model = Publication
    template_name = 'news/show_publication.html'
    context_object_name = 'publication'

class create_publication(CreateView):
    model = Publication
    fields = ['title', 'text', 'create_date', 'published_date']
    template_name = 'news/create_publication.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class update_publication(UpdateView):
    model = Publication
    fields = ['title', 'text']
    template_name = 'news/create_publication.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)        

class delete_publication(DeleteView):
    model = Publication
    success_url = '/'
