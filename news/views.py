"""
This module represents how does the website loads pages
"""
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView, UpdateView
)
from .models import Publication

class PublicationsList(ListView): # pylint: disable=too-many-ancestors
    """
    This class is a child of ListView (declared in django class)
    Used when View should use a template to show a list of instances
    of single object (model in this context)
    """
    model = Publication
    template_name = 'news/publications_list.html'
    context_object_name = 'publications'
    ordering = ['-published_date']
    paginate_by = 5

class PublicationView(DetailView): # pylint: disable=too-many-ancestors
    """
    This class is a child of DetailView (declared in django class)
    Used when View should use a template to show a single page with
    information of single object in the format declared in template
    """
    model = Publication
    template_name = 'news/show_publication.html'
    context_object_name = 'publication'

class CreatePublication(CreateView): # pylint: disable=too-many-ancestors
    """
    This class is a child of CreateView (declared in django class)
    Used when View should use a template to show a form with fields
    specified in list fields = [] to create the instance of some object

    def form_valid is a function to validate the data input in form
    """
    model = Publication
    fields = ['title', 'text', 'create_date', 'published_date']
    template_name = 'news/create_publication.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePublication(UpdateView): # pylint: disable=too-many-ancestors
    """
    This class is a child of UpdateView (declared in django class)
    Used when View should use a template to show a form with data you want
    to update
    """
    model = Publication
    fields = ['title', 'text']
    template_name = 'news/create_publication.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeletePublication(DeleteView): # pylint: disable=too-many-ancestors
    """
    This class is a child of DeleteView (declared in django class)
    Used when View should use a template to delete an object of some instance
    and redirect to a success_url route
    """
    model = Publication
    success_url = '/'
